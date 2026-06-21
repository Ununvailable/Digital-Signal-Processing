'''
Q5. y(t) = 10*cos(2*pi*f1*t) + 5*cos(2*pi*f2*t) + noise(t)
    f1 = 10 Hz, f2 = 20 Hz
    noise(t): uniform noise in [-1, 1]
    fs = 100 Hz

Tasks:
    - Plot combined signal overlaid with its component signals.
    - Plot the noise.
    - Plot power spectral density: Periodogram vs Welch method.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram, welch

# ===========================================================================================================

fs = 100
t  = np.linspace(0, 1, fs, endpoint=False)

f1, f2 = 10, 20
x1 = 10 * np.cos(2 * np.pi * f1 * t)
x2 = 5 * np.cos(2 * np.pi * f2 * t)

np.random.seed(0)
noise = np.random.uniform(-1, 1, size=len(t))

y = x1 + x2 + noise

# ===========================================================================================================

# Plot combined signal vs component signals
# Ans: x1 dominates in amplitude (10 vs 5) and oscillates slower (10 Hz vs 20 Hz);
#      y(t) shows the superposition with added high-frequency noise jitter.
plt.figure(figsize=(10, 5))
plt.plot(t, y,  label='y(t) = x1+x2+noise', color='black', linewidth=1.0)
plt.plot(t, x1, label='x1(t), A=10, f1=10Hz', linestyle='--')
plt.plot(t, x2, label='x2(t), A=5, f2=20Hz', linestyle='--')
plt.title('Combined Signal vs Component Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ===========================================================================================================

# Plot the noise
plt.figure(figsize=(10, 3))
plt.plot(t, noise, color='gray', linewidth=0.8)
plt.title('Uniform Noise η(t), range [-1, 1]')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================================================================================================

# Power Spectral Density: Periodogram vs Welch
f_per, Pxx_per   = periodogram(y, fs)
f_wel, Pxx_wel   = welch(y, fs, nperseg=fs // 2)

plt.figure(figsize=(10, 5))
plt.semilogy(f_per, Pxx_per, label='Periodogram', alpha=0.8)
plt.semilogy(f_wel, Pxx_wel, label='Welch', linewidth=2)
plt.title('Power Spectral Density: Periodogram vs Welch')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (V^2/Hz)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Ans: The Periodogram (single-segment FFT) has high frequency resolution but high
#      variance - the noise floor is jagged and erratic.
#      Welch's method averages PSD estimates over overlapping segments, trading
#      frequency resolution for significantly reduced variance, giving a smoother,
#      more statistically reliable estimate of the noise floor while still clearly
#      resolving the peaks at f1=10 Hz and f2=20 Hz.
