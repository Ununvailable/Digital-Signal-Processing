import numpy as np
import wave
import struct
import scipy.signal as signal
import matplotlib.pyplot as plt

def chirp_signal(duration, f_start=0, f_end=100, fs=1000, type='linear'):
   num_samples = duration * fs	# 樣本數
   t = np.linspace(0, duration, num_samples, endpoint = False )
   x = 3000*signal.chirp(t, f_start, t1, f_end, type) # linear chirp

   return x, num_samples, t

# ----------------------------------------------------
#  DSP 模組
# ----------------------------------------------------	
f0 = 0						# 初始頻率(Hz)
f1 = 2000					# 終止頻率(Hz)
t1 = 2
duration = 5				# 時間長度(秒)
fs = 44100					# 取樣頻率(Hz)
chirp_type = 'linear'       # chirp type = 'linear, 'logarithmic', 'hyperbolic', 'quadratic

x, num_samples, t = chirp_signal(duration, f_start=f0, f_end=f1, fs=fs, type='linear')

file = "chirp.wav"		# 檔案名稱
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"			# 壓縮型態
compname = "not compressed"	# 無壓縮

with wave.open(file, 'w' ) as wav_file:
   wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname )) 
   for s in x :
      wav_file.writeframes(struct.pack('h', int(s)))

# Plot the sine wave
plt.figure()
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Chirp wave")
plt.grid(True)
plt.show()	