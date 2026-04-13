import numpy as np
import wave
import struct
import scipy.signal as signal
import numpy.random as random
import matplotlib.pyplot as plt

file = "chirp.wav"			# 檔案名稱
file_noisy = "chirp_impulse.wav"			# 檔案名稱

amplitude = 6000			# 音量大小
f0 = 0						# 初始頻率(Hz)
f1 = 1000					# 終止頻率(Hz)
duration = 1				# 時間長度(秒)
fs = 44100					# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"			# 壓縮型態
compname = "not compressed"	# 無壓縮

t = np.linspace( 0, duration, num_samples, endpoint = False)
chirp_signal0 = signal.chirp(t, f0, duration, f1, 'linear') # linear chirp
x = amplitude*chirp_signal0

# Add impulse noise
# Create a 1D signal with impulse noise
signal_length = len(chirp_signal0)
impulse = np.zeros(signal_length)
num_impulses = int(0.05*signal_length) # 10%
impulse_indices = np.random.randint(0, signal_length, num_impulses) # find indices
impulse[impulse_indices] = np.random.randint(-3, 5, num_impulses)  # Varying amplitude impulses

y0 = chirp_signal0 + impulse # add noise

y = amplitude*y0

print(f"max_y = {int(max(y))}")
print(f"min_y = {int(min(y))}")

with wave.open(file, 'w') as wav_file:
   wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname)) 
   for s_x in x:
      wav_file.writeframes(struct.pack('h', int(s_x)))

with wave.open(file_noisy, 'w') as wav_file_n:
   wav_file_n.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname)) 
   for s_y in y:
      wav_file_n.writeframes(struct.pack('h', int(s_y)))


plt.figure(1)										
plt.plot(t, chirp_signal0)
plt.title("input sinal: chirp")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 1, -2, 2 ] )

plt.figure(2)
plt.plot(t, impulse)
plt.title("noise signal: uniform distribution")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 1, -1, 1 ] )

plt.figure(3)
plt.plot(t, y0)
plt.title("output signal with added noise: y(t)")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 1, -12, 12 ] )

plt.show( )