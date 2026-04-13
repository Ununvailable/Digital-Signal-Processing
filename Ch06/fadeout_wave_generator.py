import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

def fadeout(fade_out_duration):
   # Parameters
   frequency = 1  # Frequency of the sine wave
   duration = 5  # Duration of the sine wave in seconds
   sampling_rate = 100  # Samples per second
   #fade_out_duration = 4 # Duration of the fade out

   # Time vector
   t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
   # Generate sine wave
   sine_wave = np.sin(2 * np.pi * frequency * t)
   # Fade-out amplitude
   fade_out_start = duration - fade_out_duration
   fade_out = np.ones_like(t)
   alpha=1/fade_out_duration
   fade_out[t >= fade_out_start] = np.exp(-alpha*t[t >= fade_out_start])
   # Apply fade out to the sine wave
   faded_sine_wave = sine_wave * fade_out

   return faded_sine_wave, t

file = "fadeout.wav"		# 檔案名稱
fade_out_duration = 4      # Duration of the fade out
amplitude = 30000           # 音量大小
frequency = 300				# 頻率(Hz)
duration = 3				# 時間長度(秒)
fs = 44100				   	# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"		   	# 壓縮型態
compname = "not compressed" # 無壓縮

x, t = fadeout(fade_out_duration)

with wave.open(file, 'w' ) as wav_file:
   wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname )) 
   for s in x :
      wav_file.writeframes( struct.pack( 'h', int ( s ) ) )


# Plot the sine wave
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with Fade-Out Amplitude")
plt.grid(True)
plt.show()