import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Ball:
    """
    r       → radius of revolution or length of string
    x,y     → Anchor point or point about revolution
    x1,y1   → Positon of ball
    Theta   → Angle, this will be updated with animation
    """

    def __init__(self):
        self.r = 1
        self.x = self.y = 0

    def plot(self, theta):
        self.x1 = self.x + self.r * np.cos((theta / 180) * np.pi)
        self.y1 = self.y + self.r * np.sin((theta / 180) * np.pi)
        return [self.x,self.x1],[self.y,self.y1]

fig, ax = plt.subplots()
ax.set(xlim=(-2, 2), ylim=(-2, 2))
line,= ax.plot([], [])       # String
scat = ax.scatter([], [])         # Ball
ball = Ball()

print(ball.plot(90))
line.set_data(ball.plot(90))
plt.tight_layout()
plt.show()


def points(self):
    trace_step = int(500 / self.r)
    trace_points = Ball.Point[0][::trace_step], Ball.Point[1][::trace_step]
    rev_step = int(100 * self.speed / self.r)
    rev_points = Ball.Point[0][::rev_step], Ball.Point[1][::rev_step]
