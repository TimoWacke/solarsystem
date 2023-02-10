from ParticleFactory import ParticleFactory
from Simulate import Simulate
from Animate import Animate


p = ParticleFactory("Elipse")
p.removeOffsetSpeed()
s = Simulate(h=0.05, n=10000)
a = Animate(p, s.verlet)

a.create_video()
a.pathPlot()
a.energyPlot()
a.phaseSpace(True) #True to show 3d, False to show 2d
a.save_video()