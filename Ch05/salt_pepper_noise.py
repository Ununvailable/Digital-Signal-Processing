import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

amplitude = eval( input( "Enter amplitude of impulse (salt and pepper) noise: " ) )
probability = eval( input( "Enter probability of impulse noise appearance(%): " ) )

t = np.linspace( 0, 1, 200, endpoint = False )		# 定義時間陣列
x = 10 * np.cos( 2 * np.pi * 5 * t )				# 原始訊號

# Salt and pepper noise (values will be either min or max)
min_value = -10  # Pepper (black)
max_value = 10   # Salt (white)

noise = np.zeros(x.size)							# 脈衝雜訊
for i in range(x.size):
    p1 = random.uniform(0, 1)
    if p1 < probability / 100:
        p2 = random.uniform(0, 1)
        if p2 < 0.5:
            noise[i] = max_value  # Salt (white)
        else:
            noise[i] = min_value  # Pepper (black)
        
y = x + noise
            
plt.figure(1)										
plt.plot(t, x)
plt.title("Input signal: x(t)")
plt.xlabel('t (second)')
plt.ylabel('Amplitude')
plt.axis([0, 1, -12, 12])

plt.figure(2)
plt.stem(t, noise)
plt.title(f"Salt and Pepper Noise (min={min_value}, max={max_value}, probability={probability}%)")
plt.xlabel('t (second)')
plt.ylabel('Amplitude')

plt.figure(3)
plt.plot(t, y)
plt.title("Output signal with salt and pepper noise: y(t)")
plt.xlabel('t (second)')
plt.ylabel('Amplitude')
plt.axis([0, 1, -15, 15])

plt.show()