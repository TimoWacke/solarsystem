

class Data:

    def __init__(self, p_axes, p_momentum, p_radius, p_phi, energy, t_axis):

        self.p_axes = p_axes
        self.p_momentum = p_momentum
        self.p_radius = p_radius
        self.p_phi = p_phi
        self.energy = energy
        self.t_axis = t_axis
        self.xmin = self.p_axes[0][0][0]
        self.xmax = self.p_axes[0][0][0]
        self.ymin = self.p_axes[0][1][0]
        self.ymax = self.p_axes[0][1][0]
        self.zmin = self.p_axes[0][1][0]
        self.zmax = self.p_axes[0][1][0]
        for p, list in enumerate(p_axes):
            self.xmin = min(self.xmin, min(self.p_axes[p][0]))
            self.xmax = max(self.xmax, max(self.p_axes[p][0]))
            self.ymin = min(self.ymin, min(self.p_axes[p][1]))
            self.ymax = max(self.ymax, max(self.p_axes[p][1]))
            self.zmin = min(self.zmin, min(self.p_axes[p][2]))
            self.zmax = max(self.zmax, max(self.p_axes[p][2]))

    

        self.diff = max(self.xmax - self.xmin, self.ymax - self.ymin)

        self.xcenter = (self.xmax + self.xmin) / 2
        self.ycenter = (self.ymax + self.ymin) / 2

        self.qxmin = self.xcenter - (self.diff / 2)
        self.qxmax = self.xcenter + (self.diff / 2)
        self.qymin = self.ycenter - (self.diff / 2)
        self.qymax = self.ycenter + (self.diff / 2)

        self.qxmin -= self.diff * 0.05
        self.qxmax += self.diff * 0.05
        self.qymin -= self.diff * 0.05
        self.qymax += self.diff * 0.05
