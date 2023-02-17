from ParticleFactory import ParticleFactory
from Simulate import Simulate
from Animate import Animate


p = ParticleFactory("Tatoo")
p.removeOffsetSpeed()
s = Simulate(h=0.003, n=80000)
a = Animate(p, s.verlet)

a.create_video()
a.save_video()
a.pathPlot()
a.energyPlot()
a.phaseSpace(True) #True to show 3d, False to show 2d