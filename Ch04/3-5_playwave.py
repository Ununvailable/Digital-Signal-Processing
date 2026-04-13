# use pyaudio to play and record audio on a variety of platforms, 
# including Windows, Linux, and Mac. With pyaudio, playing audio is done by writing to a .Stream:
# https://realpython.com/playing-and-recording-sound-python/

import pyaudio # pip install pyaudio
import wave
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

filename = input( "For playing and plotting waveform, please enter wav file name: " )

print("plotting wave...")
# plot wave
sampling_rate, x = read(filename)

plt.plot(x )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.show( )

# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()