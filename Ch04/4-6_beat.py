import numpy as np
import matplotlib.pyplot as plt

t = np.linspace( 0, 0.1, 1000, endpoint = False )	# 定義時間陣列	

f1 = 20												# 低頻頻率
f2 = 200											# 高頻頻率
x1 = np.cos( 2 * np.pi * f1 * t )
x2 = np.cos( 2 * np.pi * f2 * t )
x = x1 * x2
envelope1 =  x1   # 包絡
envelope2 = x2

# 繪圖
fig1 = plt.figure(1)
plt.plot( t, x1, 'g-') 
plt.plot( t, x2, 'b--' )
plt.legend([f'x1: $f_1$={f1}Hz', f'x2: $f_2$={f2}Hz'])
plt.axis( [ 0, 0.1, -1, 1 ] )
plt.title("$x_1, x_2$")

fig2 = plt.figure(2)
plt.plot( t, x, '-' ) 
plt.axis( [ 0, 0.1, -1, 1 ])
plt.title("$x_1*x_2$")

fig3 = plt.figure(3)
plt.plot( t, envelope1, '--', color = 'b')
plt.plot( t, -envelope1, '--', color = 'b')
plt.axis( [ 0, 0.1, -1, 1 ] )
plt.title("upper and lower envelopes by $[-x_1, x_1]$")

fig4 = plt.figure(4)
plt.plot( t, envelope2, '--', color = 'b')
plt.plot( t, -envelope2, '--', color = 'b')
plt.axis( [ 0, 0.1, -1, 1 ] )
plt.title("upper and lower envelopes by $[-x_2, x_2]$")

fig5 = plt.figure(5)	
plt.plot( t, x, '-' ) 							
plt.plot( t, envelope1, '--', color = 'b' )
plt.plot( t, -envelope1, '--', color = 'b' )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 0.1, -1, 1 ] )
plt.title("$x_1*x_2$ covered by envelope [-$x_1$, $x_1$]")

fig6 = plt.figure(6)	
plt.plot( t, x, '-' ) 							
plt.plot( t, envelope2, '--', color = 'b' )
plt.plot( t, -envelope2, '--', color = 'b' )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 0.1, -1, 1 ] )
plt.title("$x_1*x_2$ covered by envelope [-$x_2$, $x_2$]")

plt.show( )