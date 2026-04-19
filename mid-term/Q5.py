'''
Q5. (12%) Continuing from Q4's chirp signal, add uniform noise (using NumPy's Random package).
Uniform distribution interval: [-1, 1].

Draw both signal waveforms on the same graph:
    overlay the noise-free chirp on the noisy chirp, and label each wave function.

Calculate the phasor of the noise wave: amplitude and phase shift.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# ===========================================================================================================

# Parameters (same as Q4)
fs = 1500
t = np.linspace(0, 2, fs * 2)
f0 = 1
f1 = 350
t1 = 3
phi = 0

# ===========================================================================================================

# Generate chirp (no noise)
x_chirp = chirp(t, f0=f0, f1=f1, t1=t1, method='logarithmic', phi=phi)

# Generate uniform noise on [-1, 1]
np.random.seed(42)
noise = np.random.uniform(-1, 1, size=len(t))

# Noisy chirp
x_noisy = x_chirp + noise

# ===========================================================================================================

# Draw both waveforms on the same graph (noisy first, clean on top).
# Ans:
plt.figure(figsize=(10, 4))
plt.plot(t, x_noisy,  linewidth=0.6, color='gray',       alpha=0.8, label='Noisy chirp $x_{noisy}(t)$')
plt.plot(t, x_chirp,  linewidth=0.8, color='darkorange',             label='Clean chirp $x_{chirp}(t)$')
plt.title('Chirp Signal: With and Without Uniform Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ===========================================================================================================

# Calculate the phasor of the noise wave: amplitude and phase shift.
# Ans:
# Convert the noise signal to a complex phasor representation using the discrete Fourier transform (DFT). 
# The dominant (DC) component of the noise gives the "average" phasor; alternatively we use the overall complex representation at the fundamental analysis frequency.
#
# For a random noise signal, the conventional approach is:
#   Treat the noise as a complex signal via its analytic representation,
#   then compute the mean amplitude and mean phase.

# Method: compute the FFT and find the component with maximum magnitude
N = len(noise)
noise_fft = np.fft.fft(noise) / N          # normalise
freqs = np.fft.fftfreq(N, d=1/fs)

# Index of maximum magnitude (dominant frequency component of noise)
idx = np.argmax(np.abs(noise_fft[:N // 2]))

A_noise   = 2 * np.abs(noise_fft[idx])     # factor 2: one-sided spectrum
phi_noise = np.angle(noise_fft[idx])

print("=== Phasor of the Noise Wave ===")
print(f"Dominant frequency : {freqs[idx]:.4f} Hz")
print(f"Amplitude          : {A_noise:.4f}")
print(f"Phase shift        : {phi_noise:.4f} rad  ({np.degrees(phi_noise):.2f}°)")
