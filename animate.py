import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import Verlet
import Particles
import progressBar
import sys

interval = 5000
steps = 10000
interval = 0.15
steps = int(1000 / interval)

name = "Solar"
name = "Tatoo"
name = "Elipse"
name = "Moon System"

particles = Particles.particleList(name)
particles = Particles.removeTotalImpulse(particles)

p_axes, mmin, mmax = Verlet.verlet(particles, interval, steps, name)


particleMasses = [p.mass for p in particles]
particleColors = [p.color for p in particles]
maxsize = max(particleMasses) ** (1/8)
s = list(map(lambda x: x**(1/8) / maxsize * 69, particleMasses))
c = particleColors

plt.rcParams['animation.ffmpeg_path'] = './ffmpeg.exe'


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
        self.frames = 500
        self.fps = 25
        self.skip = int(steps / self.frames)
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=int(1000/self.fps), frames=self.frames,
                                           init_func=self.setup_plot, blit=True)
        plt.show()

        if len(sys.argv) > 1 and sys.argv[1] == "-v":
            print("\n")
            print("Saving Video")
            self.ani.save('scatter.mp4', writer='ffmpeg', fps=self.fps,
                        dpi=100, metadata={'title': 'test'})

        # avoid plotting a spare static plot

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        xpositions = []
        ypositions = []
        for p in p_axes:
            xpositions.append(p[0][0])
            ypositions.append(p[1][0])
        self.scat = self.ax.scatter(xpositions, ypositions, s=s, c=c)

        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        xy = []
        progressBar.draw(
            i+1, self.frames, prefix='Rendering', suffix='Complete', length=50)
        for p in p_axes:
            xy.append([p[0][i*self.skip], p[1][i*self.skip]])
        # Set x and y data...
        self.scat.set_offsets(xy)
        if i >= self.frames - 1:
            if len(sys.argv) > 1 and sys.argv[1] == "-v":
                plt.close()
                print("\nClose graphs to save video")
        return self.scat,


a = AnimatedScatter()
