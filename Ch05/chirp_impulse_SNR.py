# prompt: calculate SNR of a chirp signal with impulse noise added

import numpy as np
import matplotlib.pyplot as plt

# Generate a chirp signal
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)
f0 = 10  # Start frequency
f1 = 50  # End frequency
chirp_signal = np.sin(2 * np.pi * (f0 + (f1 - f0) * t / (t[-1] - t[0])) * t)

# Add impulse noise
num_impulses = 10
impulse_indices = np.random.randint(0, len(chirp_signal), num_impulses)
impulse_amplitudes = np.random.randint(10, 20, num_impulses)
noisy_signal = chirp_signal.copy()
noisy_signal[impulse_indices] += impulse_amplitudes

# Calculate SNR in terms of signal power
signal_power = np.mean(chirp_signal**2)
noise_power = np.mean((noisy_signal - chirp_signal)**2)
snr = 10 * np.log10(signal_power / noise_power)

# Print SNR
print(f"SNR: {snr:.2f} dB")

# Plot the signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, chirp_signal)
plt.title('Chirp Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, noisy_signal)
plt.title('Chirp Signal with Impulse Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()