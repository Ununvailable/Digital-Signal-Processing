'''
Q4. Three input signals:
    x_k(t) = A_k * sin(2*pi*f_k*t + rho_k),  k = 1,2,3
    A_k = 5k,  f_k = 100k Hz,  rho_k = pi*(k-1)/4
    duration = 1 s, fs = 1000 Hz

For each x_k(t):
    - time-domain plot
    - magnitude vs phase spectrum (x-y axes)
    - magnitude vs phase spectrum (polar axis)

Harmonic wave:  x(t) = x_1(t) + x_2(t) + x_3(t)
Beat wave:      x(t) = x_1(t) * x_2(t) * x_3(t)
Each also plotted in time domain + x-y spectrum + polar spectrum.
'''

import numpy as np
import matplotlib.pyplot as plt

# ===========================================================================================================

fs  = 1000
t   = np.linspace(0, 1, fs, endpoint=False)

A   = {1: 5 * 1, 2: 5 * 2, 3: 5 * 3}
fk  = {1: 100 * 1, 2: 100 * 2, 3: 100 * 3}
rho = {1: np.pi * 0 / 4, 2: np.pi * 1 / 4, 3: np.pi * 2 / 4}

x = {k: A[k] * np.sin(2 * np.pi * fk[k] * t + rho[k]) for k in (1, 2, 3)}

# ===========================================================================================================

def magnitude_phase_spectrum(sig, fs):
    N = len(sig)
    X = np.fft.fft(sig)
    freqs = np.fft.fftfreq(N, d=1/fs)
    half = N // 2 + 1
    freqs = freqs[:half]
    X = X[:half]
    mag = np.abs(X) / N
    mag[1:] *= 2
    phase = np.angle(X)
    phase[mag < 1e-6] = 0
    return freqs, mag, phase

def plot_time(sig, title):
    plt.figure(figsize=(8, 3))
    plt.plot(t, sig, linewidth=0.7)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_xy_spectrum(freqs, mag, phase, title):
    fig, axs = plt.subplots(1, 2, figsize=(11, 4))
    axs[0].stem(freqs, mag)
    axs[0].set_title(f'{title} - Magnitude Spectrum')
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('Magnitude')
    axs[0].grid(True)

    axs[1].stem(freqs, phase)
    axs[1].set_title(f'{title} - Phase Spectrum')
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Phase (rad)')
    axs[1].grid(True)
    plt.tight_layout()
    plt.show()

def plot_polar_spectrum(mag, phase, title):
    plt.figure(figsize=(5, 5))
    ax = plt.subplot(111, projection='polar')
    ax.stem(phase, mag)
    ax.set_title(f'{title} - Polar Magnitude/Phase Spectrum')
    plt.tight_layout()
    plt.show()

# ===========================================================================================================
# Individual signals x_1, x_2, x_3
# ===========================================================================================================
for k in (1, 2, 3):
    name = f'x_{k}(t)'
    plot_time(x[k], name)
    freqs, mag, phase = magnitude_phase_spectrum(x[k], fs)
    plot_xy_spectrum(freqs, mag, phase, name)
    plot_polar_spectrum(mag, phase, name)
    # Ans: each x_k has a single dominant spectral line at f_k with phase = rho_k - pi/2
    #      (sine -> cosine phase shift of -pi/2 from FFT's cosine-phase reference).

# ===========================================================================================================
# Harmonic wave: sum of the three signals
# ===========================================================================================================
x_harmonic = x[1] + x[2] + x[3]
plot_time(x_harmonic, 'Harmonic Wave x(t) = x1+x2+x3')
freqs_h, mag_h, phase_h = magnitude_phase_spectrum(x_harmonic, fs)
plot_xy_spectrum(freqs_h, mag_h, phase_h, 'Harmonic Wave')
plot_polar_spectrum(mag_h, phase_h, 'Harmonic Wave')
# Ans: the harmonic spectrum shows three separate spectral lines at f1=100, f2=200,
#      f3=300 Hz, each retaining its own original amplitude and phase -
#      summation in time domain corresponds to superposition of spectral lines
#      (no new frequencies are created).

# ===========================================================================================================
# Beat wave: product of the three signals
# ===========================================================================================================
x_beat = x[1] * x[2] * x[3]
plot_time(x_beat, 'Beat Wave x(t) = x1*x2*x3')
freqs_b, mag_b, phase_b = magnitude_phase_spectrum(x_beat, fs)
plot_xy_spectrum(freqs_b, mag_b, phase_b, 'Beat Wave')
plot_polar_spectrum(mag_b, phase_b, 'Beat Wave')
# Ans: multiplication in time domain corresponds to convolution in frequency domain.
#      The beat wave spectrum therefore shows NEW spectral lines at sum/difference
#      frequencies (e.g. f1+f2+f3, |f1-f2+f3|, etc.) rather than at f1, f2, f3
#      themselves - unlike the harmonic (additive) case, the product generates an
#      intermodulated spectrum and a slowly varying amplitude envelope in time domain.
