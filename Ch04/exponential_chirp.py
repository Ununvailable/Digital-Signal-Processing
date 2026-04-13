# prompt: plot exponential chirp signal with amplitude=10

import numpy as np
import matplotlib.pyplot as plt


# Parameters
amplitude = 10
fs = 1000  # Sampling frequency
duration = 0.1  # Duration of the signal in seconds
t = np.arange(0, duration, 1/fs)  # Time vector
f0 = 10  # Starting frequency
f1 = 50  # Ending frequency

# Generate exponential chirp signal
signal = amplitude * np.sin(2 * np.pi * f0 * np.exp((np.log(f1 / f0) / duration) * t) * t)

# Plot the signal
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Exponential Chirp Signal')
plt.grid(True)
plt.show()