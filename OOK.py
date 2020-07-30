import numpy as np
from itertools import count
import matplotlib.pyplot as plt

bin_data = '10011'
# Modulating signal
mod_freq = 1
mod_signal=np.array([])
for bit in bin_data:
    mod_signal = np.append(mod_signal,np.arange(0,mod_freq))

# setting time axis
time = np.arange(0, len(bin_data)*mod_freq, 0.001)

# setting carrie wave
amp = 10
carr_freq = 10
car_wave = np.sin(2 * np.pi * time * carr_freq)


