# prompt: plot a 1d impulse noise

import numpy as np
import matplotlib.pyplot as plt


# Create a 1D signal with impulse noise
signal_length = 100
signal = np.zeros(signal_length)
num_impulses = 10
impulse_indices = np.random.randint(0, signal_length, num_impulses)
signal[impulse_indices] = np.random.randint(1, 10, num_impulses)  # Varying amplitude impulses

# Plot the signal
plt.stem(signal)  # Use stem plot for better visualization of impulses
plt.title('1D Impulse Noise')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()