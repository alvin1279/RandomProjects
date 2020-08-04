from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

class DoublePendulum:
    """
    init_state is [theta1, omega1, theta2, omega2] in degrees,

    """

    def __init__(self
                 init_state = [120,] ):


TO DO LATER AFTER STUDYING THE PHYSICS OF DOUBLE PENDULUM