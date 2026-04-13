import os
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from playsound import playsound # pip install playsound

filename = input( "For playing and plotting waveform, please enter wav file name: " )

#path ="sound_lib"
#filepath = os.path.join(path, filename)
print(filename)

# https://realpython.com/playing-and-recording-sound-python/
# play sound
playsound(filename)

print("plotting wave...")
# plot wave
sampling_rate, x = read(filename)

plt.plot( x )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.show( )