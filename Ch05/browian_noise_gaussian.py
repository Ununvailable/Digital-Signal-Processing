# prompt: generate brownian noise

import numpy as np
import matplotlib.pyplot as plt


# Generate Brownian noise data: 
# the Brownian Motion is a cumulative sum of the increments from the normal distribution
def brownian_noise(n_samples, duration=1, sample_rate=44100):
  """Generates Brownian noise data."""
  time = np.linspace(0, duration, int(duration * sample_rate))
  # the Brownian Motion is a cumulative sum of the increments from the normal distribution
  noise = np.cumsum(np.random.randn(len(time)))
  return noise


# Set the number of samples and duration
n_samples = 44100
duration = 1

# Generate the Brownian noise data
brown_noise = brownian_noise(n_samples, duration)

# Plot the Brownian noise
plt.plot(brown_noise)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Brownian Noise')
plt.show()