import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import scipy.stats as stats

#t = np.linspace( 0, 1, 200, endpoint = False )		# 定義時間陣列

# Define the parameters of the normal distribution
mu = 0  # Mean
sigma = 1  # Standard deviation
amplitude = 10
# Generate x values for the plot
t = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 200)

x = np.cos( 2 * np.pi * 5 * t/3 )				# 原始訊號
noise = random.normal(mu, sigma, 200)			    	# 雜訊(高斯分佈)

# Calculate the probability density function (PDF) for the normal distribution
#noise = stats.norm.pdf(t, mu, sigma)
#Display the histogram of the samples, along with the probability density function:
count, bins, ignored = plt.hist(noise, 30, density=True)

plt.figure(1)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title(' histogram of the samples, along with the probability density function')

# output signal
y0 = x + noise
y = amplitude*x + noise

plt.figure(2)
plt.plot(t, x, 'g--')
plt.plot(t, y0, 'b-')
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -2, 2 ] )
plt.legend(['x', '$y_0$'])

plt.figure(3)
plt.plot(t, noise )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.title('noise')
#plt.axis( [ 0, 1, -3, 3 ] )

plt.figure(4)
plt.plot(t, y-noise)
plt.plot(t, y)
plt.title('noisy signal $y$')
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -15, 15 ] )
plt.legend('[$x$, ]')
plt.show( )