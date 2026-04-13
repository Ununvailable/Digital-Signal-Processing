import numpy as np
import wave
import struct
import scipy.signal as signal

# The wave module provides a convenient interface to the Waveform Audio “WAVE” (or “WAV”) file format. 
# Only uncompressed PCM encoded wave files are supported.
file = "sawtooth1.wav"		# 檔案名稱

amplitude = 30000           # 振幅
frequency = 100         	# 頻率(Hz)
duration = 3				# 時間長度(秒)
fs = 44100					# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數

num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"			# 壓縮型態
compname = "not compressed"	# 無壓縮

t = np.linspace( 0, duration, num_samples, endpoint = False )
x = amplitude * signal.sawtooth( 2 * np.pi * frequency * t )

print(struct.pack('h', 16))
print(hex(16))

with wave.open( file, 'w' ) as wav_file:
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 
	for s in x:
		# 將整數轉成 'h': hexidecimal 數據: 
		wav_file.writeframes(struct.pack ('h', int(s)))
