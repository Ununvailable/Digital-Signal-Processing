import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal

def downsampling(x, sampling_rate=2, method=1):
	N = int( len( x ) / sampling_rate) 
	y = np.zeros( N )
	
	if method == 1:   			# Decimation 
		for n in range( N ):
			y[n] = x[sampling_rate*n]
	else:						# Averaging
		for n in range( N ):
			y[n] = ( x[sampling_rate*n] + x[sampling_rate*n+1] ) / 2	
			
	return y
	
def upsampling(x, sampling_rate=2, method=1):
	N = len( x ) * sampling_rate
	y = np.zeros( N )	
	
	if method == 1:				# Zero-Order Hold
		for n in range( N ):
			y[n] = x[int( n / sampling_rate)] 
	else:						# First order Hold (Linear Interpolation)
		for n in range( N ):
			if int( n / sampling_rate) == n / sampling_rate:
				y[n] = x[int( n / sampling_rate)]
			else:
				n1 = int( n / sampling_rate)
				n2 = n1 + 1
				if n2 < len( x ):
					y[n] = ( x[n1] + x[n2] ) / 2
				else:
					y[n] = x[n1] / 2

	return y

def resampling(x, sampling_rate):
	num = int( len(x) * sampling_rate )
	y = signal.resample(x, num)
	return y	
	
def main( ):
	infile  = input("Input File: ")	# chirp.wav
	outfile = input("Output File: ")	# chirp_ds1.wav, chirp_ds2.wav, chirp_us1.wav, chirp_us2.wav, chirp_ds_rs.wav
	
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

	# ----------------------------------------------------
	#  DSP 模組
	# ----------------------------------------------------	
	
	print( "Sampling Rate Conversion" )
	print( "(1) Downsampling by scale_factor (Decimation)" )
	print( "(2) Downsampling by scale_factor (Average)" )
	print( "(3) Upsampling by scale_factor (Zero-Order Hold)" )
	print( "(4) Upsampling by scale_factor (Linear Interpolation)" )
	print( "(5) Resampling" )
	
	choice = eval( input("Please enter your choice: "))
	if (1<=choice and choice<=4):
		print("Please input sampling rate by 2 power of 2, e.g. 2, 4,...")
		sampling_rate = eval(input( "Sampling Rate = " ) )
	elif choice == 5:
		print("Please input sampling rate, e.g. 2.5, 3.5,...")
		sampling_rate = eval(input( "Sampling Rate = " ) )

	if choice == 1:
		y = downsampling(x, sampling_rate=2, method=1)
	elif choice == 2:
		y = downsampling(x, sampling_rate=2, method=2)
	elif choice == 3:
		y = upsampling(x, sampling_rate=2, method=1)
	elif choice == 4:
		y = upsampling(x, sampling_rate=2, method=2)
	elif choice == 5:
		y = resampling( x, sampling_rate)
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