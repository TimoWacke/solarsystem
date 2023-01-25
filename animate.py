import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import ParticleFactory
import progressBar

class Animate:
    """Animated scatter plot and charts using matplotlib.animations.FuncAnimation.

        @params
            particleFactory  - Required  : array of Objects from Particle Class (Particle)
            simulator        - Required  : method like Simulate.verlet(), that returns data arrays
    """

    def __init__(self, particleFactory: ParticleFactory.ParticleFactory, simulator):
        self.particleFactory = particleFactory
        self.p_axes, self.p_momentum, self.p_radius, self.p_phi, self.energy, self.t_axis, self.mmin, self.mmax = simulator(
            particleFactory.particleList)
        self.n = len(self.t_axis)
        self.h = np.round(self.t_axis[1]-self.t_axis[0], 3)
        self.mmin -= (self.mmax - self.mmin) * 0.05
        self.mmax += (self.mmax - self.mmin) * 0.05
        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(10)
        self.fig.set_figwidth(10)
        plt.xlim([self.mmin, self.mmax])
        plt.ylim([self.mmin, self.mmax])
        # Then setup FuncAnimation.
        self.frames = 500
        self.fps = 25
        self.skip = int(self.n / self.frames)
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=int(1000/self.fps), frames=self.frames,
                                           init_func=self.setup_plot, blit=True)

        # avoid plotting a spare static plot

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        xs = []
        ys = []
        for p in self.p_axes:
            xs.append(p[0][0])
            ys.append(p[1][0])
        self.scat = self.ax.scatter(
            xs, ys, s=self.particleFactory.sizes, c=self.particleFactory.colors)
        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        xy = []
        progressBar.draw(
            i+1, self.frames, prefix='Rendering', suffix='Complete', length=50)
        for p in self.p_axes:
            xy.append([p[0][i*self.skip], p[1][i*self.skip]])
        # Set x and y data...
        self.scat.set_offsets(xy)

        return self.scat,

    def pathPlot(self):

        fig, ax = plt.subplots()

        for p, pt in enumerate(self.particleFactory.particleList):
            ax.plot(self.p_axes[p][0],  self.p_axes[p]
                    [1], c=pt.color, linewidth=2, label=pt.name)
        fig.set_figwidth(10)
        fig.set_figheight(10)
        plt.xlim([self.mmin, self.mmax])
        plt.ylim([self.mmin, self.mmax])
        plt.legend()

        plt.title(
            '{} - {} steps, dt={}'.format(self.particleFactory.name, self.n, self.h))
        plt.show()
        plt.savefig(
            'images/{} - {} steps, dt={}.png'.format(self.particleFactory.name, self.n, self.h))
        plt.close()

    def energyPlot(self):
        fig2, ax2 = plt.subplots()
        ax2.plot(self.t_axis, self.energy, 'r-', label='energy')
        plt.xlabel("time")
        plt.ylabel("total energy in system")
        plt.title(
            '{} - {} steps, dt={}'.format(self.particleFactory.name, self.n, self.h))
        plt.show()
        plt.savefig(
            'images/{} - {} steps, dt={}_energy.png'.format(self.particleFactory.name, self.n, self.h))
        plt.close()

    def save_video(self):
        print("\n")
        print("Saving Video")
        self.ani.save('scatter.mp4', writer='ffmpeg', fps=self.fps,
                      dpi=100, metadata={'title': 'test'})

    def phaseSpace(self, is3d):
        if (is3d):
            fig3 = plt.figure()
            ax3 = fig3.add_subplot(projection='3d')

            for p, pt in enumerate(self.particleFactory.particleList):
                ax3.scatter(self.p_radius[p], self.p_phi[p],
                            self.p_momentum[p], c=pt.color, s=4, label=pt.name)

            ax3.set_xlabel("radius")
            ax3.set_ylabel("phi")
            # ax3.set_zlabel("phi")
            plt.title(
                '{} - {} steps, dt={}'.format(self.particleFactory.name, self.n, self.h))
            plt.legend()
            plt.show()
            plt.savefig(
                'images/{} - {} steps, dt={}_phase.png'.format(self.particleFactory.name, self.n, self.h))
            plt.close()
        else:
            fig3, ax3 = plt.subplots()
            for p, pt in enumerate(self.particleFactory.particles):
                ax3.plot(self.p_radius[p], self.p_momentum[p],
                         c=pt.color, label=pt.name)

            plt.xlabel("radius")
            plt.ylabel("momentum")
            plt.title(
                '{} - {} steps, dt={}'.format(self.particleFactory.name, self.n, self.h))
            plt.legend()
            plt.savefig(
                'images/{} - {} steps, dt={}_phase.png'.format(self.particleFactory.name, self.n, self.h))
            plt.close()

        return (self.p_axes, self.mmin, self.mmax)
