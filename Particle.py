import numpy as np

class Particle:
    
    """
    Physics for a Particle and it's interaction with another

    @params
        name        - Required  : name of the particle set
        mass        - Required  : mass        
        coord       - Required  : coordinates in dict {x: , y: , z: }    
        velocity    - Required  : velocity in dict {x: , y: , z: }
        color       - Required  : HEX code, or Color name
    """

    def __init__(self, name: str, mass: float, coord: dict, velocity: dict, color: str):
        self.name = name
        self.mass = mass
        self.coord = np.array([coord["x"], coord["y"], coord["z"]])
        self.velocity = np.array([velocity["x"], velocity["y"], velocity["z"]])
        self.color = color

    def move(self, dt: float):

        """
        Applies a movement with the particles currently set velocity
        for the timestep of dt to it.

        @params
            dt          - Required  : time for which the velocity should be applied to the coordinates
        """ 

        delta = self.velocity * dt
        self.coord = self.coord + delta

    def kineticEnergy(self) -> float:
        """
        returns the particles current kinetic energy
        """ 
        return self.mass / 2 * np.linalg.norm(self.velocity)**2

    def momentum(self) -> np.array:
        """
        returns the particles current momentum vector
        """
        return self.mass * self.velocity

    def phi(self) -> float:
        """
        returns the particles current angle in radian relative to the coordinate system
        """
        radianHalf = np.arccos(self.coord[0] / np.linalg.norm(np.array([self.coord[0], self.coord[1]])) )
        if self.coord[1] < 0:
            return 2 * np.pi - radianHalf
        return radianHalf 

    def potEnergy(self, otherParticle: 'Particle') -> float:
        """
        returns the particles current potential energy in the gravity field of the other particle

        @params
            otherParticle : the particle with the gravity field
        """
        diff = np.subtract(self.coord, otherParticle.coord)
        radius = np.linalg.norm(diff)
        return - self.mass * otherParticle.mass / radius

    def accelerate(self, other: 'Particle', dt: float):
        """
        adjusts the velocity of two particles, based on the gravity force they apply to each other.

        @params
            otherParticle : the particle that's responsible for the acceleration
        """
        diff = np.subtract(other.coord, self.coord)
        radius = np.linalg.norm(diff)
        self.velocity = self.velocity + diff * other.mass * dt / (radius**3)
        other.velocity = other.velocity - diff * self.mass * dt / (radius**3)
        # return force that applys on self

    def __repr__(self): 
        return '{} - mass: {}, pos: {}, vel: {}'.format(self.name, self.mass, str(self.coord), str(self.velocity))

    def __str__(self): 
        return '{} - mass: {}, pos: {}, vel: {}'.format(self.name, self.mass, str(self.coord), str(self.velocity))
