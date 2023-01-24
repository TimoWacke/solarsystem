import numpy as np
import Solar as sol


class Particle:
    def __init__(self, name, mass, coord, velocity, color):
        self.name = name
        self.mass = mass
        self.coord = np.array([coord["x"], coord["y"], coord["z"]])
        self.velocity = np.array([velocity["x"], velocity["y"], velocity["z"]])
        self.color = color

    def move(self, dt):
        # delta is the distance the particle is moved by in the timestep dt
        delta = self.velocity * dt
        self.coord = self.coord + delta

    def kineticEnergy(self):
        return self.mass / 2 * np.linalg.norm(self.velocity)**2

    def impulse(self):
        return self.mass * self.velocity

    def potEnergy(self, otherParticle):
        diff = np.subtract(self.coord, otherParticle.coord)
        radius = np.linalg.norm(diff)
        return - self.mass * otherParticle.mass / radius

    def accelerate(self, other, dt):
        diff = np.subtract(other.coord, self.coord)
        radius = np.linalg.norm(diff)
        self.velocity = self.velocity + diff * other.mass * dt / (radius**3)
        other.velocity = other.velocity - diff * self.mass * dt / (radius**3)
        # return force that applys on self
        # return f_abs * (diff/radius)


def particleList(name):

    if name == "Solar":
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
        return [star, mercury, venus, earth, mars, jupiter, saturn, uranus, moon]

    if name == "Tatoo":
        sun1 = Particle("Tatoo I", 50, {"x": 0, "y": 10, "z": 0}, {
                        "x": -1, "y": 0, "z": 0}, "peachpuff")
        sun2 = Particle(
            "Tatoo II", 50, {"x": 0, "y": -10, "z": 0}, {"x": 1, "y": 0, "z": 0}, "orange")
        planet = Particle("Planet", 1, {"x": 100, "y": 0, "z": 0}, {
                          "x": 0, "y": 1, "z": 0}, "cadetblue")

        return [sun1, sun2]
        return [sun1, sun2, planet]

    if name == "Elipse":
        star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                        "x": 0, "y": 0, "z": 0}, "orange")
        planet = Particle("Pluto", 1, {"x": 100, "y": 0, "z": 0}, {
                        "x": 0, "y": 1.3, "z": 0}, "cadetblue")

        # return [sun1, sun2]
        return [star, planet]

    if name == "Moon System":
        star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                        "x": 0, "y": 0, "z": 0}, "orange")
        planet = Particle("Planet", 10, {"x": 100, "y": 0, "z": 0}, {
                        "x": 0, "y": 3, "z": 0}, "cadetblue")
        moon = Particle("Moon", 1, {"x": 100, "y": 4, "z": 0}, {
                        "x": 1, "y": 3, "z": 0}, "black")
        return [star, planet, moon]
    
    if name == "Lagrangepoints":
        star = Particle("Star", 1000, {"x": 0, "y": 0, "z": 0}, {
                        "x": 0, "y": 0, "z": 0}, "yellow")
        planet = Particle("Planet", 7, {"x": 100, "y": 0, "z": 0}, {
                        "x": 0, "y": 3, "z": 0}, "green")
        #l1 = Particle("L1", 0.01, {"x": 100/(sqrt(50)+1)*sqrt(50), "y": 0, "z": 0}, {
        #                "x": 0, "y": 3/(sqrt(50)+1)*sqrt(50), "z": 0}, "black")
        #l2 = Particle("L2", 0.01, {"x": 100, "y": 0, "z": 0}, {
        #                "x": 0, "y": 3, "z": 0}, "black")
        l3 = Particle("L3", 0.01, {"x": -100, "y": 0, "z": 0}, {
                        "x": 0, "y": -3, "z": 0}, "black")
        l4 = Particle("L4", 0.01, {"x": 100*np.cos(np.pi/3), "y":-100*np.sin(np.pi/3) , "z": 0}, {
                        "x": 3*np.sin(np.pi/3), "y": 3*np.cos(np.pi/3), "z": 0}, "black")
        l5 = Particle("L5", 0.01, {"x": 100*np.cos(np.pi/3), "y":100*np.sin(np.pi/3) , "z": 0}, {
                        "x": -3*np.sin(np.pi/3), "y": 3*np.cos(np.pi/3), "z": 0}, "black")
        return [star, planet, l3, l4, l5]

def removeTotalImpulse(particleList):
    totalImpulse = np.array([float(0), float(0), float(0)])
    totalMass = 0
    for p in particleList:
        totalImpulse = np.add(totalImpulse, p.impulse())
        totalMass += p.mass
    totalVelocity = totalImpulse / totalMass
    for p in particleList:
       p.velocity = np.subtract(p.velocity, totalVelocity)
    return particleList