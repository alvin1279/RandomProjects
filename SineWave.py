import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import numpy as np

# Plot Initialisation
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(-1, 1))
ax.set_autoscale_on(False)

#  Sine wave initialisation
freq = .1
Amp = 1
time = count(0)


def animate(_):
    global time
    t = next(time)/10           # Incrementing time at 0.1 intervals
    ax.clear()
    ax.set(xlim=(0, 10), ylim=(-1, 1))
    ax.scatter(t, np.sin(2 * np.pi * (t * freq)))

    if t >= 10:                  # Resetting when it crosses plot border
        time = count(0)


ani = FuncAnimation(fig, animate, interval=10)
plt.show()
