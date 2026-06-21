'''
Q2. Magnitude Spectrum and Phase Spectrum for signals (a)-(d).
    t = 1 second, fs = 100 Hz.

(a) Sine wave:      x(t) = 3*cos(2*pi*20*t + pi/4)
(b) Harmonic wave:  x(t) = 10 + 8*cos(2*pi*50*t) + 4*cos(2*pi*150*t)
(c) Square wave:    A = 1, f = 10 Hz
(d) Beat wave:      x(t) = 2*cos(2*pi*25*t)*cos(2*pi*50*t)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# ===========================================================================================================

fs = 100
t  = np.linspace(0, 1, fs, endpoint=False)

# (a) Sine wave
x_a = 3 * np.cos(2 * np.pi * 20 * t + np.pi / 4)

# (b) Harmonic wave (DC component An = 10)
x_b = 10 + 8 * np.cos(2 * np.pi * 50 * t) + 4 * np.cos(2 * np.pi * 150 * t)

# (c) Square wave
x_c = 1 * square(2 * np.pi * 10 * t)

# (d) Beat wave
x_d = 2 * np.cos(2 * np.pi * 25 * t) * np.cos(2 * np.pi * 50 * t)

signals = {
    '(a) Sine Wave'   : x_a,
    '(b) Harmonic Wave': x_b,
    '(c) Square Wave' : x_c,
    '(d) Beat Wave'   : x_d,
}

# ===========================================================================================================

def magnitude_phase_spectrum(x, fs):
    N = len(x)
    X = np.fft.fft(x)
    freqs = np.fft.fftfreq(N, d=1/fs)

    # keep only non-negative frequencies
    half = N // 2 + 1
    freqs = freqs[:half]
    X = X[:half]

    mag = np.abs(X) / N
    mag[1:] *= 2          # one-sided amplitude scaling (skip DC)
    phase = np.angle(X)
    phase[mag < 1e-6] = 0  # zero-out phase for negligible magnitude bins

    return freqs, mag, phase

# ===========================================================================================================

for name, x in signals.items():
    freqs, mag, phase = magnitude_phase_spectrum(x, fs)

    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    axs[0].stem(freqs, mag)
    axs[0].set_title(f'{name} - Magnitude Spectrum')
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('Magnitude')
    axs[0].grid(True)

    axs[1].stem(freqs, phase)
    axs[1].set_title(f'{name} - Phase Spectrum')
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Phase (rad)')
    axs[1].grid(True)

    fig.suptitle(name)
    plt.tight_layout()
    plt.show()
