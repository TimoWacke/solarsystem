import progressBar 
import numpy as np
import matplotlib.pyplot as plt

offsetspeed = np.array([000, 000, 0])


def verlet(particles, h, n):

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
    for p in particles:
        p_axes.append([np.zeros(n), np.zeros(n), np.zeros(n)])

    for pti in particles:
        for ptj in particles: 
            if ptj == pti:
                break
            #force = pti.gravityForce(ptj)
            #ptj.accelerate(-force, h/2)
            #pti.accelerate(force, h/2)
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
    mmin -= (mmax - mmin) / 25
    mmax += (mmax - mmin) / 25
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.xlim([mmin, mmax])
    plt.ylim([mmin, mmax])
    plt.legend()
    plt.draw()

    fig2 , ax2 = plt.subplots()
    ax2.plot(t_axis, energy, 'r-', label='energy')
    
    plt.legend()
    plt.draw()

    return (p_axes, mmin, mmax)
