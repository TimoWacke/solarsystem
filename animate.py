import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import Verlet
import Particles

interval = 0.25
steps = 10000
particles = Particles.particleList()
p_axes, mmin, mmax = Verlet.verlet(particles, interval, steps)


particleSizes = []
particleColors = []
maxmass = 0
for pt in particles:
    particleSizes.append(pt.mass)
    particleColors.append(pt.color)
    maxmass = max(maxmass, pt.mass)
maxmass = maxmass**(1/10)
s = list(map(lambda x: x**(1/10) / maxmass * 60, particleSizes))
print(s)
c = particleColors


plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'


class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""

    def __init__(self, numpoints=steps):
        self.numpoints = numpoints
        self.particles = particles

        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(10)
        self.fig.set_figwidth(10)
        plt.xlim([mmin, mmax])
        plt.ylim([mmin, mmax])
        # Then setup FuncAnimation.
        self.skip = int(steps / 500)
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=25, frames=500,
                                           init_func=self.setup_plot, blit=True)
        self.ani.save('scatter.mp4', writer='ffmpeg', fps=30,
                      dpi=100, metadata={'title': 'test'})
        plt.close()                   # avoid plotting a spare static plot

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        xpositions = []
        ypositions = []
        for p in p_axes:
            xpositions.append(p[0][0])
            ypositions.append(p[1][0])
        # Set x and y data...
        self.scat = self.ax.scatter(xpositions, ypositions, s=s, c=c)
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.

        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        xy = []
        if (i*self.skip/steps*100) % 10 == 0:
            print(i*self.skip/steps*100, "%", i)
        for p in p_axes:
            xy.append([p[0][i*self.skip], p[1][i*self.skip]])
        # Set x and y data...
        self.scat.set_offsets(xy)
        # Set sizes...

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,


a = AnimatedScatter()
plt.show()
