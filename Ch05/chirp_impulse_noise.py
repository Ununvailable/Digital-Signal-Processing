# prompt: generate a chirp signal with impulse noise added

import numpy as np
import matplotlib.pyplot as plt

# Parameters for chirp signal
fs = 1000  # Sampling frequency
duration = 1  # Duration of the signal in seconds
t = np.arange(0, duration, 1/fs)  # Time vector
f0 = 10  # Starting frequency
f1 = 50  # Ending frequency

# Generate chirp signal
chirp_signal = np.sin(2 * np.pi * (f0 + (f1 - f0) * t / duration) * t)

# Add impulse noise
num_impulses = 10
impulse_indices = np.random.randint(0, len(chirp_signal), num_impulses)
impulse_amplitudes = np.random.randint(-10, 10, num_impulses)
chirp_signal[impulse_indices] += impulse_amplitudes

# Plot the signal
plt.plot(t, chirp_signal)
plt.title('Chirp Signal with Impulse Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()