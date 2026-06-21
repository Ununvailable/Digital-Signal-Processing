'''
Q3. IIR filter application - Echo system.

Input: x(t) = A*cos(2*pi*f*t), A = 10, f = 5 Hz
       duration = 2 s, fs = 44100 Hz

(a) Echo every 1 s, 5 echoes, decreasing amplitude, total output length = 10 s.
    Save as Q3-1.wav
(b) Echo every 0.5 s, 10 echoes, total output length = 10 s.
    Save as Q3-2.wav
'''

import os
import numpy as np
from scipy.io import wavfile

# ===========================================================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

A  = 10
f  = 5
fs = 44100
dur_in  = 2     # seconds (input signal duration)
dur_out = 10    # seconds (total output length)

t_in = np.arange(0, dur_in, 1 / fs)
x = A * np.cos(2 * np.pi * f * t_in)

# ===========================================================================================================

def echo_filter(x, fs, dur_out, delay_sec, n_echoes, decay=0.6):
    '''
    IIR echo system: y[n] = x[n] + sum_{k=1}^{n_echoes} decay^k * x[n - k*D]
    D = delay in samples corresponding to delay_sec.
    Output is zero-padded to fill dur_out seconds.
    '''
    N_out = int(fs * dur_out)
    D = int(fs * delay_sec)

    x_pad = np.zeros(N_out)
    x_pad[:len(x)] = x

    y = np.copy(x_pad)
    for k in range(1, n_echoes + 1):
        shift = k * D
        if shift >= N_out:
            break
        gain = decay ** k
        y[shift:] += gain * x_pad[:N_out - shift]

    return y

# ===========================================================================================================

def save_audio(path, fs, y):
    y = y / (np.max(np.abs(y)) + 1e-12)
    wavfile.write(path, fs, (y * 32767).astype(np.int16))

# ===========================================================================================================

# (a) Echo every 1 s, 5 echoes, total length = 10 s
y_a = echo_filter(x, fs, dur_out, delay_sec=1.0, n_echoes=5, decay=0.6)
save_audio(os.path.join(SCRIPT_DIR, 'Q3-1.wav'), fs, y_a)

# (b) Echo every 0.5 s, 10 echoes, total length = 10 s
y_b = echo_filter(x, fs, dur_out, delay_sec=0.5, n_echoes=10, decay=0.7)
save_audio(os.path.join(SCRIPT_DIR, 'Q3-2.wav'), fs, y_b)

print("Q3-1.wav and Q3-2.wav have been saved.")
print("Open both files in Audacity to inspect echo amplitude decay and time spacing.")

# ===========================================================================================================
# Ans (echo amplitude & time spacing):
# (a) Echoes occur every 1.0 s; amplitude of the k-th echo = 0.6^k * A
#     (k = 1..5), decaying geometrically: 6, 3.6, 2.16, 1.296, 0.778 (relative to A=10).
# (b) Echoes occur every 0.5 s; amplitude of the k-th echo = 0.7^k * A
#     (k = 1..10), decaying more slowly than (a) but with twice the echo density,
#     producing a denser, longer-sustained echo tail.
