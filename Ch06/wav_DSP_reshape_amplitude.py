import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal

def fadeout(x, sampling_rate, fade_out_duration):
    # Time vector
    t = np.linspace(0, duration, len(x), endpoint=False)
    # Fade-out amplitude
    fade_out_start = duration - fade_out_duration
    fade_out = np.ones_like(t)
    alpha=1/fade_out_duration
    fade_out[t >= fade_out_start] = np.exp(-alpha*t[t >= fade_out_start])
    # Apply fade out to the x wave
    faded_wave = x * fade_out

    return faded_wave, t

def AM(x, fc, fs ):
	t = np.zeros( len( x ) )
	for i in range( len( x ) ):
		t[i] = i / fs
	carrier = np.cos( 2 * np.pi * fc * t )
	return x * carrier

def resampling(x, sampling_rate):
	num = int( len(x) * sampling_rate )
	y = signal.resample(x, num)
	return y	
	
def main( ):
	infile  = input("Input File: ")	# chirp.wav
	outfile = input("Output File: ")	# chirp_fadeout.wav, chirp_am.wav
	
	# ----------------------------------------------------
	#  輸入模組
	# ----------------------------------------------------	
	wav = wave.open( infile, 'rb' )
	num_channels = wav.getnchannels( )	# 通道數
	sampwidth	 = wav.getsampwidth( )	# 樣本寬度
	fs			 = wav.getframerate( )	# 取樣頻率(Hz)
	num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
	comptype	 = wav.getcomptype( )	# 壓縮型態
	compname	 = wav.getcompname( )	# 無壓縮
	wav.close( )

	sampling_rate, x = read( infile )	# 輸入訊號
    duration = num_frames/sampling_rate

	# ----------------------------------------------------
	#  DSP 模組
	# ----------------------------------------------------	
	
	print( "Non-perioidc Signal Conversion" )
	print( "(1) Fadeout" )
	print( "(2) Amplitude Modulation" )
	
	choice = eval( input("Please enter your choice: "))
	
	if choice == 1:
        _fade_out_duration_p = eval( input("Enter fadeout duration: "))
        fade_out_duration = duration/_fade_out_duration_p
		y = fadeout(x, sampling_rate, fade_out_duration)
	elif choice == 2:
        fc = eval( input( "Enter carrier frequency (Hz) for AM: " ) )
		y = AM(x, fc, fs )
	else:
		print( "Your choice is not supported!" )
		y = x

	num_frames = len( y )
		
	# ----------------------------------------------------
	#  輸出模組
	# ----------------------------------------------------		
	wav_file = wave.open(outfile, 'w' )
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname)) 

	with wave.open(outfile, 'w' ) as wav_file:
		wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname)) 
		for s in y:
			wav_file.writeframes( struct.pack('h', int (s)))
	
main( )