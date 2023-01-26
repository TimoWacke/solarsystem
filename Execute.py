from ParticleFactory import ParticleFactory
from Simulate import Simulate
from Animate import Animate


p = ParticleFactory("Solar")
p.removeOffsetSpeed()
s = Simulate(h=1500, n=100000)
a = Animate(p, s.verlet)

a.pathPlot()
a.energyPlot()
a.phaseSpace(True) #True to show 3d, False to show 2d
a.save_video()