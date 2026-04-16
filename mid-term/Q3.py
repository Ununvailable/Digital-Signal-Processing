'''
Q3. (26%) If the beat wave is defined as:

    x(t) = A·cos(2π·f1·t) + A·cos(2π·f2·t)

Where amplitude A = 3, frequency f1 = 10 Hz, f2 = 200 Hz.
Use Python to implement, display time t = 0~0.2 s, sampling frequency fs = 5000 Hz.

(12%) Draw the two overlapping sine waves on the same graph and label each wave function.
(7%)  Draw the beat wave waveform.
(7%)  Draw the beat wave envelope, i.e. overlay the low-frequency signal waveform on the beat wave.
'''

import numpy as np
import matplotlib.pyplot as plt

# ===========================================================================================================

# Parameters
A  = 3
f1 = 10     # Hz (low frequency)
f2 = 200    # Hz (high frequency)
fs = 5000   # Hz (sampling frequency)
t  = np.linspace(0, 0.2, int(fs * 0.2))

# ===========================================================================================================

# Component waves
x1 = A * np.cos(2 * np.pi * f1 * t)
x2 = A * np.cos(2 * np.pi * f2 * t)

# Beat wave: sum of the two components
x_beat = x1 + x2

# Envelope: the beat wave can be written as
#   x(t) = 2A·cos(2π·f_mod·t)·cos(2π·f_carrier·t)
# where f_mod = (f2 - f1) / 2 = 95 Hz  and  f_carrier = (f2 + f1) / 2 = 105 Hz
# The envelope (low-frequency amplitude modulation) is:
#   envelope(t) = 2A·|cos(2π·f_mod·t)|
f_mod     = (f2 - f1) / 2   # 95 Hz
f_carrier = (f2 + f1) / 2   # 105 Hz
envelope  = 2 * A * np.abs(np.cos(2 * np.pi * f_mod * t))

# ===========================================================================================================

# (12%) Draw the two overlapping sine waves on the same graph.
# Ans:
plt.figure(figsize=(10, 4))
plt.plot(t, x1, label=r'$x_1(t)=3\cos(2\pi \cdot 10 \cdot t)$', linewidth=1)
plt.plot(t, x2, label=r'$x_2(t)=3\cos(2\pi \cdot 200 \cdot t)$', linewidth=0.8, alpha=0.7)
plt.title('Two Overlapping Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# (7%) Draw the beat wave waveform.
# Ans:
plt.figure(figsize=(10, 4))
plt.plot(t, x_beat, color='steelblue', linewidth=0.8, label=r'$x(t)=x_1(t)+x_2(t)$')
plt.title('Beat Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# (7%) Draw the beat wave envelope overlaid on the beat wave.
# Ans:
plt.figure(figsize=(10, 4))
plt.plot(t, x_beat,   color='steelblue', linewidth=0.6, alpha=0.8, label=r'Beat wave $x(t)$')
plt.plot(t,  envelope, color='red',       linewidth=1.5, label=r'Envelope $2A|\cos(2\pi \cdot 95 \cdot t)|$')
plt.plot(t, -envelope, color='red',       linewidth=1.5, linestyle='--')
plt.title('Beat Wave with Envelope')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
