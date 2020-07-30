import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



# Plot Initialisation
fig, ax = plt.subplots()
ax.set(xlim=(-50, 50), ylim=(-50, 50))
ax.set_autoscale_on(False)

# whirl Initialisation
x,y = [],[]
line,= ax.plot([],[])           # This returns a plot line inside a list hence unpacink
print(line)
def animate(i):
    t = 0.1*i

    xvalue = t*np.cos(t)
    yvalue = t*np.sin(t)


    x.append(xvalue)
    y.append(yvalue)
    line.set_data(x,y)
    return line,                # To do blitting return needs to be given, i dont know why though


ani = FuncAnimation(fig, animate, interval=10, blit=True, frames=500)
ax.axis('off')
plt.show()
