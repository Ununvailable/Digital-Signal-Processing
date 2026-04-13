import numpy as np
import wave
import struct
import scipy.signal as signal
import numpy.random as random
import matplotlib.pyplot as plt

file = "chirp.wav"			# 檔案名稱
file_noisy = "chirp_uniform.wav"			# 檔案名稱

amplitude = 15000			# 音量大小
f0 = 0						# 初始頻率(Hz)
f1 = 1000					# 終止頻率(Hz)
duration = 3				# 時間長度(秒)
t1 = 5
fs = 44100					# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
t = np.linspace( 0, duration, num_samples, endpoint = False)
chirp0 = signal.chirp(t, f0, t1, f1, 'linear') # linear chirp
chirp = amplitude*chirp0

noise = random.uniform(-1, 1, num_samples)				# 雜訊(均勻分佈)	
chirp_noisy0 = chirp0 + noise

chirp_noisy = amplitude*chirp_noisy0

print(f"max_chirp_noisy = {int(max(chirp_noisy))}")
print(f"min_chirp_noisy = {int(min(chirp_noisy))}")

# method 1: Save original and noisy signals as a WAV file using wave 
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"			# 壓縮型態
compname = "not compressed"	# 無壓縮

with wave.open(file, 'w') as wav_file:
   wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname)) 
   for s_x in chirp:
      wav_file.writeframes(struct.pack('h', int(s_x)))

with wave.open(file_noisy, 'w') as wav_file_n:
   wav_file_n.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname)) 
   for s_y in chirp_noisy:
      wav_file_n.writeframes(struct.pack('h', int(s_y)))


# method 2:Save the original and noisy signal as a WAV file using wavefile
import scipy.io.wavfile as wavfile
wavfile.write('chirp1.wav', fs, chirp.astype(np.float32))
wavfile.write('chirp_uniform1.wav', fs, chirp_noisy.astype(np.float32))

plt.figure(1)										
plt.plot(t, chirp0)
plt.title("input sinal: x(t)")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -2, 2 ] )

plt.figure(2)
plt.plot(t, noise)
plt.title("noise signal: uniform distribution")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -1, 1 ] )

plt.figure(3)
plt.plot(t, chirp_noisy0)
plt.title("chirp signal with added noise: y(t)")
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 1, -12, 12 ] )

plt.show( )