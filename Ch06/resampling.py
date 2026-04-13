import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def resampling( x, sampling_rate ):
	num = int( len(x) * sampling_rate )
	y = signal.resample(x, num )
	return y

def main(resampling_dactor):
	x = np.array([ 1, 2, 4, 3, 2, 1, 2, 1 ])
	t1 = list(range(len(x)))
	y = resampling( x, resampling_factor)
	t2 = list(range(len(y)))
	plt.figure( 1 )
	plt.stem(x)
	
	plt.figure( 2 )
	plt.stem(y)
	
	plt.figure(3)
	plt.title(f'resampling by factor={resampling_factor}')
	plt.plot(t1, x, 'b-*', label = 'x(n)')
	plt.plot(t2, y, 'r-*', label = 'y(n)')
	plt.legend(['x(n)', 'y(n)'])
	plt.show( )

resampling_factor = 1.5	
main(resampling_factor)	