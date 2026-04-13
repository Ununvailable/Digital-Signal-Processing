import numpy as np
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 1000, endpoint = False )	# 定義時間陣列

x = np.cos( 2 * np.pi * 5 * t )					# 產生弦波
a = np.linspace( 1, 0, 1000, endpoint = False ) # 產生淡出陣列 
x_fade_out = x * a                    # 套用淡出效果 
x_fade_in = x * ( 1 - a )              # 套用淡入效果

plt.figure(1)
plt.plot(t, x)
plt.figure(2)							
plt.plot( t, x_fade_out )
plt.plot( t, x_fade_in )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.legend(['x_fade_out', 'x_fade_in'])
plt.axis( [ 0, 1, -1.2, 1.2 ] )

plt.show( )