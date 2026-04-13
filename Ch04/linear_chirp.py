# prompt: plot linear chirp signal

import numpy as np
import matplotlib.pyplot as plt
import struct, wave

# Parameters
amplitude = 30000  # 音量大小
fs = 44100  # Sampling frequency
duration = 5  # Duration of the signal in seconds
t = np.arange(0, duration, 1/fs)  # Time vector
f0 = 10  # Starting frequency
f1 = 1000  # Ending frequency

# Generate linear chirp signal
chirp_signal = amplitude * np.sin(2 * np.pi * (f0 + (f1 - f0) * t / duration) * t)

# Plot the signal
plt.plot(t, chirp_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Linear Chirp Signal')
plt.grid(True)
plt.show()

file = "linear_chirp.wav"

# create wav
#fs = 44100					# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"			# 壓縮型態
compname = "not compressed"	# 無壓縮

with wave.open(file, 'w' ) as wav_file:
   wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname )) 
   for s in chirp_signal :
      wav_file.writeframes(struct.pack('h', int(s)))