# prompt: generate a chirp signal corrupted by brownian noise

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Parameters for chirp signal
amplitude = 15000
f_start = 0  # Starting frequency
f_end = 1000  # Ending frequency
t_end = 5     # end time
duration = 3  # Duration of the signal in seconds
sample_rate = 44100  # Sample rate

# Generate time vector
t = np.linspace(0, duration, int(duration * sample_rate))

# Generate chirp signal
#chirp_signal = np.sin(2 * np.pi * (f_start + (f_end - f_start) * t / duration) * t)
chirp_signal0 = signal.chirp(t, f_start, t_end, f_end, 'linear')
chirp_signal = amplitude * chirp_signal0

# Parameters for Brownian noise
noise_level = 0.05  # Adjust this to control the intensity of the noise

# Generate Brownian noise
brownian_noise = np.cumsum(np.random.randn(len(t)))
brownian_noise = noise_level * brownian_noise / np.std(brownian_noise)  # Normalize noise amplitude

# Corrupt chirp signal with Brownian noise
corrupted_signal = chirp_signal + brownian_noise
print(len(brownian_noise))
print(len(chirp_signal))

corrupted_signal = amplitude*corrupted_signal

print(min(corrupted_signal))
print(max(corrupted_signal))

# Plot the signals
plt.figure(figsize=(10, 6))
plt.plot(t, chirp_signal, label="Chirp Signal")
plt.plot(t, corrupted_signal, label="Chirp Signal with Brownian Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Chirp Signal Corrupted by Brownian Noise")
plt.legend()
plt.grid(True)

# Optional: Save the Brownian noise as a WAV file
import scipy.io.wavfile as wavfile
wavfile.write('chirp2.wav', sample_rate, chirp_signal.astype(np.float32))
wavfile.write('chirp_brownian.wav', sample_rate, corrupted_signal.astype(np.float32))

plt.show()