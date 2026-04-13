import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy.random as random

f0=0
f1=5
t1=5
fs=1000
duration = 3
num_samples = duration * fs	# 樣本數

t = np.linspace( 0, duration, num_samples, endpoint = False )	# 定義時間陣列
x = signal.chirp( t, f0, f1, t1, 'linear' )		# 產生啁啾訊號
noise = random.uniform(-1, 1, num_samples)				# 雜訊(均勻分佈)	
y = x + noise

fig1 = plt.figure(1)
plt.plot(t, x, 'r--')

fig2 = plt.figure(2)
plt.plot(t, y, 'b--')
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 5, -1.5, 1.5 ] )

plt.show( )