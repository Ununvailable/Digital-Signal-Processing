import numpy as np
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 1000, endpoint = False )	# 定義時間陣列
theta1 = 2 * np.pi * 5 * t
theta2 = theta1 + 2*np.pi
x1 = np.cos( theta1 )					# 產生弦波
x2 = np.cos( theta2 )					# 產生弦波
plt.plot(t, x1, 'g-')								# 繪圖
plt.plot(t, x2, 'b--')
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
#plt.axis( [ 0, 1, -1.2, 1.2 ] )

plt.show( )