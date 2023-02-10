import numpy as np
from Particle import Particle
import progressBar

from DataResults import Data

class Simulate:
    """
    Class for Simulations

    @params
        h           - Required  : size of timestep (float)
        n           - Required  : number of timesteps (int)
    """

    def __init__(self, h: float, n: int ):
      
        self.h = h
        self.n = n

    def verlet(self, particles: list[Particle]) -> Data:
        
        """
        Calculates the movement of particles with Verlet algorithm
        Returns positions in multidimensional array [particle p][dimension 0-2][timestep i].
        Returns maximum and minimum of the coordinates too
       
        @params
            particles      - Required  : list of Particle Objects
        """

        mmin = np.amin(particles[0].coord)
        mmax = np.amax(particles[0].coord)
        t_axis = np.linspace(0, self.n*self.h, num=self.n)
        energy = np.zeros(self.n)
        p_axes = []
        p_momentum = []
        p_radius = []
        p_phi = []

        center =  np.array([float(0), float(0), float(0)])
        masssum = 0
        for p in particles:
            p_axes.append([np.zeros(self.n), np.zeros(self.n), np.zeros(self.n)])
            masssum += p.mass
            center += p.coord * p.mass 
            p_momentum.append(np.zeros(self.n))
            p_phi.append(np.zeros(self.n))
            p_radius.append(np.zeros(self.n))
        center *= (1/masssum)

        for pti in particles:
            for ptj in particles: 
                if ptj == pti:
                    break
                # Vor dem Ersten Schritt die Beschleunigung für einen halben Zeitschritt auf den Körper anwenden.
                pti.accelerate(ptj, self.h/2)
        for i in range(self.n):
            for pt in particles:
                pt.move(self.h)
            for pti in particles:
                for ptj in particles: 
                    if pti == ptj:
                        break
                    energy[i] += pti.potEnergy(ptj)
                    #force = pti.gravityForce(ptj)
                    #pti.accelerate(force, self.h)
                    #ptj.accelerate(force, self.h)
                    pti.accelerate(ptj, self.h)
            for p, pt in enumerate(particles):
                energy[i] += pt.kineticEnergy()
                p_momentum[p][i] = np.linalg.norm(pt.momentum())
                p_radius[p][i] = np.linalg.norm(np.subtract(pt.coord, center) )
                p_phi[p][i] = pt.phi()
                p_axes[p][0][i] = pt.coord[0]
                p_axes[p][1][i] = pt.coord[1]
                p_axes[p][2][i] = pt.coord[2]
                mmin = min(mmin, np.amin(pt.coord))
                mmax = max(mmax, np.amax(pt.coord))
            if (i+1)/self.n*100%5 == 0: 
                progressBar.draw(i, self.n, "Verlet", "Complete", length=50)

        return Data(p_axes, p_momentum, p_radius, p_phi, energy, t_axis, mmin, mmax)


    # useful if you create a Pendulum class to experiment
    def verletPendulum(self, pendulumList: list) -> Data:
            
        """
        Calculates the movement of pendulums with Verlet algorithm
        Returns positions in multidimensional array [particle p][dimension 0-2][timestep i].
        Returns maximum and minimum of the coordinates too
       
        """

        mmin = pendulumList[0].phi
        mmax = pendulumList[0].phi
        t_axis = np.linspace(0, self.n*self.dt, num=self.n) # a list for each timestep to fill in with it's timevalue
        energy = np.zeros(self.n)  # a list for each timestep to fill in with the total energy of the system 
        p_axes = [] # for every particle a list of dimensions. And for each dimension a list with all timesteps to fill in coordinates
        p_momentum = [] # for every particle a list with all timesteps to fill in with the absolute values of momentum
        p_radius = []  # for every particle a list with all timesteps to fill in with the readius to the center
        p_phi = []  # for every particle a list with all timesteps to fill in with the angles relative to the coordinate system

      
        for p in pendulumList:
            p_axes.append(np.zeros(self.n)) 
            p_momentum.append(np.zeros(self.n))
            p_phi.append(np.zeros(self.n))
            p_radius.append(np.zeros(self.n))

        for p in pendulumList:
            p.accelerate(self.dt/2)

        # Iterate for each timestep    
        for i in range(self.n):

            for p in pendulumList:
                p.move(self.dt)            
                p.accelerate(self.dt/2)
            

            # put the new data on the record
            for p, pl in enumerate(pendulumList):
                energy[i] += pl.energy()
                p_momentum[p][i] = pl.v
                p_radius[p][i] = pl.length
                p_phi[p][i] = pl.phi
                p_axes[p][i] = pl.phi
                mmin = min(mmin,pl.phi)
                mmax = max(mmax, pl.phi)

            # update the progress bar after every 5% progress
            if (i+1)/self.n*100%5 == 0: 
                progressBar.draw(i, self.n, "Pendulum", "Complete", length=50)
        return Data(p_axes, p_momentum, p_radius, p_phi, energy, t_axis, mmin, mmax)