# Ball objects revolve around a fixed point
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
from matplotlib.animation import FuncAnimation
from itertools import cycle


class Ball:
    """
    r       → radius of revolution or length of string
    rmax    → biggest Radius among created instances
    speed   → No. of points  per frame
    x,y     → Anchor point or point about revolution
    x1,y1   → Position of ball
    Theta   → Angles
    Point   → [cos,sin] points about 3600, precalculated
    """
    x = y = 0

    # Pre calculation points
    theta = np.arange(0, 360, 0.1)
    sin = np.sin((theta / 180) * np.pi)
    cos = np.cos((theta / 180) * np.pi)
    Point = [cos, sin]

    def __init__(self, radius=1, speed=1, cl=True, trace=False):
        global rmax
        self.r = radius
        self.speed = speed
        self.cl = cl
        self.scat = ax.scatter([], [], c='r', s=100, zorder=2)
        self.rev_points()
        self.trace(trace)

        if rmax < self.r:
            rmax = self.r
            ax.set(xlim=(-(rmax + int(rmax * 0.1)), (rmax + int(rmax * 0.1))),
                   ylim=(-(rmax + int(rmax * 0.1)), (rmax + int(rmax * 0.1))))

    def trace(self, trace):

        if trace:
            trace_step = int(500 / self.r)
            trace_points = Ball.Point[0][::trace_step], Ball.Point[1][::trace_step]
            ax.scatter(trace_points[0] * self.r, trace_points[1] * self.r, s=1)

    def plot(self):

        if self.cl:
            self.scat.set_offsets([next(self.rev_point[0]) * self.r, next(self.rev_point[1]) * self.r])
        else:
            self.scat.set_offsets([next(self.rev_point[1]) * self.r, next(self.rev_point[0]) * self.r])
        return self.scat

    def rev_points(self):
        rev_step = int(100 * self.speed / self.r)
        self.rev_point = cycle(Ball.Point[0][::rev_step]), cycle(Ball.Point[1][::rev_step])


# Plot Initialisation,write this as an class function
rmax = 20
fig, ax = plt.subplots()
ax.set(xlim=(-(rmax + 1), (rmax + 1)), ylim=(-(rmax + 1), (rmax + 1)))
ax.set_autoscale_on(False)
ax.set_aspect('equal', adjustable='box')

# Object Initialisation
ball1 = Ball(10, trace=True, speed=5)
ball2 = Ball(15, speed=5)
ball3 = Ball(20, speed=10, cl=False)
ball4 = Ball(30, speed=2,trace=True)


def animate(_):
    a = ball1.plot()
    b = ball2.plot()
    c = ball3.plot()
    d = ball4.plot()
    return a, b, c, d


ani = FuncAnimation(fig, animate, interval=10, blit=True)

plt.show()
