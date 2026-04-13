import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 1000 )			# 定義時間陣列
f = 5
# x = signal.square( 2 * np.pi * f * t )	# 產生方波
x = np.sign(np.sin(2*np.pi*f*t))

plt.plot( t, x )						# 繪圖
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -1.2, 1.2 ] )

plt.show( )