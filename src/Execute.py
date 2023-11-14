from ParticleFactory import ParticleFactory
from Simulate import Simulate
from Animate import Animate


p = ParticleFactory("Solar")
p.removeOffsetSpeed()
s = Simulate(h=86400, n=10000)
a = Animate(p, s.verlet)

a.create_video()
a.save_video()
a.pathPlot()
a.energyPlot()
#a.phaseSpace()