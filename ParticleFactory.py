from Particle import Particle
import numpy as np
import Solar as sol

class ParticleFactory:
    
    """
    Class to handle a set of particle and use it in a simulation

    @params
        name        - Required  : name of the predefined particle set \in {"Solar", "Tatoo", "Elipse", "Moon System", "Lagrangepoints", "Phase Room"}
    """

    def __init__(self, name: str):
        self.name = name
        self.particleList = []
        self.setParticles()
        self.setSizeAndColor()

    def setSizeAndColor(self):
        try:
            self.colors = [p.color for p in self.particleList]
            self.masses = [p.mass for p in self.particleList]
            maxsize = max(self.masses) ** (1/8)
            self.sizes = list(map(lambda x: x**(1/8) / maxsize * 69, self.masses))
        except:
            self.sizes = [1] * len(self.particleList)
            self.colors = ["black"] * len(self.particleList)

    def importParticles(self, particles: list[Particle]):
        self.particleList = particles
        self.setSizeAndColor()

    def setParticles(self):
        if self.name == "Solar":
            star = Particle("Sun", sol.mass_sun, {"x": 0, "y": 0, "z": 0}, {
                            "x": 0, "y": 0, "z": 0}, "yellow")
            # star = Particle("sun", 1000, {"x": 0, "y": 0, "z": 0 },{"x": -0.001, "y": 0, "z": 0 } )
            mercury = Particle("Mercury", sol.mass_mercury, {"x": 0, "y": sol.distance_mercury, "z": 0}, {
                "x": sol.velocity_mercury, "y": 0, "z": 0}, "#DDCC44")
            venus = Particle("Venus", sol.mass_venus, {"x": 0, "y": sol.distance_venus, "z": 0}, {
                "x": sol.velocity_venus, "y": 0, "z": 0}, "#884400")
            earth = Particle("Earth", sol.mass_earth, {"x": 0, "y": sol.distance_earth, "z": 0}, {
                "x": sol.velocity_earth, "y": 0, "z": 0}, "steelblue")
            mars = Particle("Mars", sol.mass_mars, {"x": 0, "y": sol.distance_mars, "z": 0}, {
                            "x": sol.velocity_mars, "y": 0, "z": 0}, "#EE1111")
            jupiter = Particle("Jupiter", sol.mass_jupiter, {"x": 0, "y": sol.distance_jupiter, "z": 0}, {
                "x": sol.velocity_jupiter, "y": 0, "z": 0}, "chocolate")
            saturn = Particle("Saturn", sol.mass_saturn, {"x": 0, "y": sol.distance_saturn, "z": 0}, {
                "x": sol.velocity_saturn, "y": 0, "z": 0}, "goldenrod")
            uranus = Particle("Uranus", sol.mass_uranus, {"x": 0, "y": sol.distance_uranus, "z": 0}, {
                "x": sol.velocity_uranus, "y": 0, "z": 0}, "lightseagreen")
            neptune = Particle("Neptune", sol.mass_neptune, {"x": 0, "y": sol.distance_neptune, "z": 0}, {
                "x": sol.velocity_neptune, "y": 0, "z": 0}, "cornflowerblue")
            moon = Particle("Moon", sol.mass_moon, {"x": sol.distance_moon, "y": sol.distance_earth, "z": 0}, {
                            "x": sol.velocity_earth, "y": sol.velocity_moon, "z": 0}, "#666666")
            self.particleList = [star, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, moon]

        if self.name == "Tatoo":
            sun1 = Particle("Tatoo I", 50, {"x": 0, "y": 10, "z": 0}, {
                            "x": -1, "y": 0, "z": 0}, "peachpuff")
            sun2 = Particle(
                "Tatoo II", 50, {"x": 0, "y": -10, "z": 0}, {"x": 1, "y": 0, "z": 0}, "orange")
            planet = Particle("Planet", 1, {"x": 100, "y": 0, "z": 0}, {
                "x": 0, "y": 1, "z": 0}, "cadetblue")

            self.particleList = [sun1, sun2]
            #self.particleList =[sun1, sun2, planet]

        if self.name == "Elipse":
            star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                            "x": 0, "y": 0, "z": 0}, "orange")
            planet = Particle("Pluto", 1, {"x": 100, "y": 0, "z": 0}, {
                "x": 0, "y": 1.3, "z": 0}, "cadetblue")

            self.particleList = [star, planet]

        if self.name == "Moon System":
            star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                            "x": 0, "y": 0, "z": 0}, "orange")
            planet = Particle("Planet", 10, {"x": 100, "y": 0, "z": 0}, {
                "x": 0, "y": 3, "z": 0}, "cadetblue")
            moon = Particle("Moon", 1, {"x": 100, "y": 4, "z": 0}, {
                            "x": 1, "y": 3, "z": 0}, "black")
            self.particleList = [star, planet, moon]

        if self.name == "Lagrangepoints":
            star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                            "x": 0, "y": 0, "z": 0}, "yellow")
            planet = Particle("Planet", 7, {"x": 100, "y": 0, "z": 0}, {
                "x": 0, "y": 3, "z": 0}, "green")
            # l1 = Particle("L1", 0.01, {"x": 100/(sqrt(50)+1)*sqrt(50), "y": 0, "z": 0}, {
            #                "x": 0, "y": 3/(sqrt(50)+1)*sqrt(50), "z": 0}, "black")
            # l2 = Particle("L2", 0.01, {"x": 100, "y": 0, "z": 0}, {
            #                "x": 0, "y": 3, "z": 0}, "black")
            l3 = Particle("L3", 0.01, {"x": -100, "y": 0, "z": 0}, {
                "x": 0, "y": -3, "z": 0}, "black")
            l4 = Particle("L4", 0.01, {"x": 100*np.cos(np.pi/3), "y": -100*np.sin(np.pi/3), "z": 0}, {
                "x": 3*np.sin(np.pi/3), "y": 3*np.cos(np.pi/3), "z": 0}, "black")
            l5 = Particle("L5", 0.01, {"x": 100*np.cos(np.pi/3), "y": 100*np.sin(np.pi/3), "z": 0}, {
                "x": -3*np.sin(np.pi/3), "y": 3*np.cos(np.pi/3), "z": 0}, "black")
            self.particleList = [star, planet, l3, l4, l5]

        if self.name == "Phase Room":
            parts = [Particle("Star", 100000, {"x": 0, "y": 0, "z": 0}, {
                "x": 0, "y": 0, "z": 0}, "yellow")]

            for i in range(10):
                parts.append(Particle("Planet {}".format(i), 1, {"x": 0, "y": (
                    i+1)*500, "z": 0}, {"x": 10-i, "y": 0, "z": 0}, '#' + str(i)*6))
            self.particleList = parts

    def removeOffsetSpeed(self):
        """
        Determindes the velocity of the center of mass of the particle set.
        Offsets all particles velocity by the negative of this velocity.
        This sets the total momentum of the particle set to zero.
        """
        totalMomentum = np.array([float(0), float(0), float(0)])
        totalMass = 0
        for p in self.particleList:
            totalMomentum = np.add(totalMomentum, p.momentum())
            totalMass += p.mass
        totalVelocity = totalMomentum / totalMass
        for p in self.particleList:
            p.velocity = np.subtract(p.velocity, totalVelocity)

    def __repr__(self):
        pretty = "--------------------------------------------------\n"
        pretty += "Particle Factory - " + self.name + "\n"
        for p in self.particleList:
            pretty += "\t" + str(p) + "\n"
        pretty += "--------------------------------------------------\n"
        return pretty