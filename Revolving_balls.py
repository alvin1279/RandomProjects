# Ball objects revolve around a fixed point
import numpy as np
import matplotlib.pyplot as plt
import secrets

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
    resol   → increases the total number of points, increased for larger radius(int(radius/4))
    Theta   → Total no of points, for each object depends on its resol
    self.Point   → [cos,sin] 
    """
    x = y = 0

    def __init__(self, radius=1, speed=1, cl=True, trace=False):
        global rmax
        self.r = radius
        self.speed = speed
        self.cl = cl
        self.color = '#' + secrets.token_hex(3)
        
        self.scat = ax.scatter([], [], c=self.color, s=100, zorder=2)     
        self.resol = int(self.r/4)
        self.calc_points(self.resol)
        self.rev_points()
        self.trace(trace)

        if rmax < self.r:
            rmax = self.r
            ax.set(xlim=(-(rmax + int(rmax * 0.1)), (rmax + int(rmax * 0.1))),
                   ylim=(-(rmax + int(rmax * 0.1)), (rmax + int(rmax * 0.1))))

    def trace(self, trace):

        if trace:
            trace_step = int(1000 / self.r) * self.resol
            trace_points = self.Point[0][::trace_step], self.Point[1][::trace_step]
            ax.scatter(trace_points[0] * self.r, trace_points[1] * self.r, s=1, c=self.color)

    def plot(self):

        if self.cl:
            self.scat.set_offsets([next(self.rev_point[0]) * self.r, next(self.rev_point[1]) * self.r])
        else:
            self.scat.set_offsets([next(self.rev_point[1]) * self.r, next(self.rev_point[0]) * self.r])
        return self.scat

    def rev_points(self):
        rev_step = self.speed * 10 * self.resol
        self.rev_point = cycle(self.Point[0][::rev_step]), cycle(self.Point[1][::rev_step])
        
    def calc_points(self,resol=1):
        
        step = 0.1
        theta = np.arange(0, 360, step/resol)
        sin = np.sin((theta / 180) * np.pi)
        cos = np.cos((theta / 180) * np.pi)
        self.Point = [cos, sin]

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


anim = FuncAnimation(fig, animate, interval=10, blit=True)

# #saving
anim.save('Balls.gif',fps=30)
plt.show()
