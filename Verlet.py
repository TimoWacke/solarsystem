import progressBar 
import numpy as np
import matplotlib.pyplot as plt




def verlet(particles, h, n, name):

    """
    Calculates the movement of particles with Verlet algorithm
    Returns positions in multidimensional array [particle p][dimension 0-2][timestep i].
    Returns maximum and minimum of the coordinates too
    @params
        particles   - Required  : array of Objects from Particle Class (Particle)
        h           - Required  : size of timestep (float)
        n           - Required  : number of timesteps (Str)
    """

    mmin = np.amin(particles[0].coord)
    mmax = np.amax(particles[0].coord)
    t_axis = np.linspace(0, n*h, num=n)
    energy = np.zeros(n)
    p_axes = []
    p_impulses = []
    p_radius = []
    p_phi = []

    center =  np.array([float(0), float(0), float(0)])
    masssum = 0
    for p in particles:
        p_axes.append([np.zeros(n), np.zeros(n), np.zeros(n)])
        masssum += p.mass
        center += p.coord * p.mass 
        p_impulses.append(np.zeros(n))
        p_phi.append(np.zeros(n))
        p_radius.append(np.zeros(n))
    center *= (1/masssum)

    for pti in particles:
        for ptj in particles: 
            if ptj == pti:
                break
            pti.accelerate(ptj, h/2)
    for i in range(n):
        for pt in particles:
            pt.move(h)
        for pti in particles:
            for ptj in particles: 
                if pti == ptj:
                    break
                energy[i] += pti.potEnergy(ptj)
                #force = pti.gravityForce(ptj)
                #pti.accelerate(force, h)
                #ptj.accelerate(force, h)
                pti.accelerate(ptj, h)
        for p, pt in enumerate(particles):
            energy[i] += pt.kineticEnergy()
            p_impulses[p][i] = np.linalg.norm(pt.impulse())
            p_radius[p][i] = np.linalg.norm(np.subtract(pt.coord, center) )
            p_phi[p][i] = pt.phi()
            p_axes[p][0][i] = pt.coord[0]
            p_axes[p][1][i] = pt.coord[1]
            p_axes[p][2][i] = pt.coord[2]
            mmin = min(mmin, np.amin(pt.coord))
            mmax = max(mmax, np.amax(pt.coord))
        if (i+1)/n*100%5 == 0: 
            progressBar.draw(i, n, "Verlet", "Complete", length=50)

   
    fig , ax = plt.subplots()



    for p, pt in enumerate(particles):
        ax.plot(p_axes[p][0],  p_axes[p][1], c=pt.color, label=pt.name) 
    mmin -= (mmax - mmin) * 0.05
    mmax += (mmax - mmin) * 0.05
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.xlim([mmin, mmax])
    plt.ylim([mmin, mmax])
    plt.legend()

    plt.title('{} - {} steps, dt={}'.format(name, n, h))
    plt.savefig('images/{} - {} steps, dt={}.png'.format(name, n, h))
    plt.close()

    fig2 , ax2 = plt.subplots()
    ax2.plot(t_axis, energy, 'r-', label='energy')
    plt.xlabel("time")
    plt.ylabel("total energy in system")
    plt.title('{} - {} steps, dt={}'.format(name, n, h))
    plt.savefig('images/{} - {} steps, dt={}_energy.png'.format(name, n, h))
    plt.close()
    
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(projection='3d')

    for p, pt in enumerate(particles):
        ax3.scatter(p_radius[p], p_phi[p], p_impulses[p], c=pt.color, s=4, label=pt.name)

    ax3.set_xlabel("radius")
    ax3.set_ylabel("impulse")
    #ax3.set_zlabel("phi")
    plt.title('{} - {} steps, dt={}'.format(name, n, h))
    plt.legend()
    plt.show()
    plt.savefig('images/{} - {} steps, dt={}_phase.png'.format(name, n, h))
    #plt.close()

    return (p_axes, mmin, mmax)

