'''
Q1. AM sample-rate conversion test on violin.wav (carrier fc = 1250 Hz).

Place violin.wav in the same folder as this script.
Outputs (saved to the same folder):
    Q1-dsp_2.wav,  Q1-dsp_4.wav    Decimation downsample (rate 2, 4)
    Q1-asp_2.wav,  Q1-asp_4.wav    Average downsample (rate 2, 4)
    Q1-0hsp_2.wav, Q1-0hsp_4.wav   Zero-order hold upsample (rate 2, 4)
    Q1-1hsp_2.wav, Q1-1hsp_4.wav   First-order hold upsample (rate 2, 4)
    Q1-ftsp_0.7.wav, Q1-ftsp_3.5.wav  Fourier-transform resample (rate 0.7, 3.5)
'''

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample

# ===========================================================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IN_FILE    = os.path.join(SCRIPT_DIR, 'violin.wav')
fc         = 1250  # carrier frequency (Hz)

# ===========================================================================================================

def load_audio(path):
    fs, x = wavfile.read(path)
    if x.ndim > 1:          # mix down to mono
        x = x.mean(axis=1)
    x = x.astype(np.float64)
    x /= np.max(np.abs(x))  # normalize to [-1, 1]
    return fs, x

def save_audio(path, fs, x):
    x = x / np.max(np.abs(x) + 1e-12)
    wavfile.write(path, int(fs), (x * 32767).astype(np.int16))

# ===========================================================================================================

fs, x = load_audio(IN_FILE)
t = np.arange(len(x)) / fs

# AM modulation: x_am(t) = x(t) * cos(2*pi*fc*t)
x_am = x * np.cos(2 * np.pi * fc * t)

# Plot original sampled signal and AM-modulated signal
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x, linewidth=0.5)
plt.title('Original Sampled Signal (violin.wav)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, x_am, linewidth=0.5, color='darkorange')
plt.title(f'AM Modulated Signal (fc = {fc} Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================================================================================================
# Down-sampling Method 1: Decimation (take every Mth sample)
# ===========================================================================================================
for M in (2, 4):
    x_dec = x_am[::M]
    fs_dec = fs / M
    save_audio(os.path.join(SCRIPT_DIR, f'Q1-dsp_{M}.wav'), fs_dec, x_dec)

# ===========================================================================================================
# Down-sampling Method 2: Average (block-average every M samples)
# ===========================================================================================================
for M in (2, 4):
    n_blocks = len(x_am) // M
    x_avg = x_am[:n_blocks * M].reshape(-1, M).mean(axis=1)
    fs_avg = fs / M
    save_audio(os.path.join(SCRIPT_DIR, f'Q1-asp_{M}.wav'), fs_avg, x_avg)

# ===========================================================================================================
# Up-sampling Method 1: Zero-order hold (repeat each sample L times)
# ===========================================================================================================
for L in (2, 4):
    x_0h = np.repeat(x_am, L)
    fs_0h = fs * L
    save_audio(os.path.join(SCRIPT_DIR, f'Q1-0hsp_{L}.wav'), fs_0h, x_0h)

# ===========================================================================================================
# Up-sampling Method 2: First-order hold (linear interpolation between samples)
# ===========================================================================================================
for L in (2, 4):
    n_new = (len(x_am) - 1) * L + 1
    old_idx = np.arange(len(x_am))
    new_idx = np.linspace(0, len(x_am) - 1, n_new)
    x_1h = np.interp(new_idx, old_idx, x_am)
    fs_1h = fs * L
    save_audio(os.path.join(SCRIPT_DIR, f'Q1-1hsp_{L}.wav'), fs_1h, x_1h)

# ===========================================================================================================
# Resampling Method: Fourier transform based (scipy.signal.resample)
# ===========================================================================================================
for rate in (0.7, 3.5):
    n_new = int(len(x_am) * rate)
    x_ft = resample(x_am, n_new)
    fs_ft = fs * rate
    save_audio(os.path.join(SCRIPT_DIR, f'Q1-ftsp_{rate}.wav'), fs_ft, x_ft)

print("All Q1 sample-rate converted audio files have been saved.")
