# Ball attached to a string revolve around an anchor point
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from matplotlib.animation import FuncAnimation

class Ball:
    """
    r       → radius of revolution or length of string
    x,y     → Anchor point or point about revolution
    x1,y1   → Position of ball
    Theta   → Angle, this will be updated with animation
    """

    def __init__(self,radius = 1):
        self.r = radius
        self.x = self.y = 0

    def point(self,theta=0):
        self.x1 = self.x + self.r * np.cos((theta / 180) * np.pi)
        self.y1 = self.y + self.r * np.sin((theta / 180) * np.pi)
        return [self.x, self.x1], [self.y, self.y1]

# Initialisation
radius=10
fig, ax = plt.subplots()

ax.set(xlim=(-(radius+1),(radius+1)), ylim=(-(radius+1), (radius+1)))
ax.set_autoscale_on(False)
ax.set_aspect('equal', adjustable='box')

line,= ax.plot([], [],zorder=1)
scat = ax.scatter([], [],c='r',s=300,zorder=2)
ball = Ball(radius)


def animate(theta):
    points = ball.point(theta)                      #([x,x1][y,y1])
    line.set_data(points)                           # Drawing string
    scat.set_offsets([points[0][1],points[1][1]])   # Drawing Ball
    return line,scat


ani = FuncAnimation(fig, animate, interval=50,blit=True)
plt.show()
