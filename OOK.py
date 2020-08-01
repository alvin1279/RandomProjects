import numpy as np
import matplotlib.pyplot as plt

# Plot Initialisation
fig, (ax1, ax2, ax3) = plt.subplots(3, 1,sharex=True)

# Modulating signal
bin_str = '101011010'
bin_data =np.array([int(x) for x in bin_str])[:, np.newaxis]
sign_length = np.ones(1000,dtype=int)[np.newaxis,:]  # no. of points each bits occupy
signal = (bin_data*sign_length).ravel()
# Time axis generation , Used to make the carrier wave
total_points = len(signal)  # Total no.of points to be in the graph. Depends on length of binary data
step_size = .01
length = total_points * step_size
time = np.arange(0, length, step_size)

# Carrier signal
amp = 10
car_time = 100 * step_size  # to make carrier time period a factor of step size
car_signal = amp * np.sin(2 * np.pi * (time / car_time))

# Modulated signal
mod_sign = signal * car_signal

ax1.plot(time, signal)
ax2.plot(time, car_signal)
ax3.plot(time, mod_sign)
plt.show()
