# prompt: generate brownian noise

import numpy as np
import matplotlib.pyplot as plt


# Generate Brownian noise data:
def brownian_noise(n_samples, duration=1, sample_rate=44100):
  """Generates Brownian noise data."""
  time = np.linspace(0, duration, int(duration * sample_rate))
  noise = np.cumsum(np.random.randn(len(time)))
  return noise


# Set the number of samples and duration
n_samples = 44100
duration = 10

# Generate the Brownian noise data
brown_noise = brownian_noise(n_samples, duration)

# Plot the Brownian noise
plt.plot(brown_noise)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Brownian Noise')

# Optional: Save the Brownian noise as a WAV file
import scipy.io.wavfile as wavfile
wavfile.write('brown_noise.wav', 44100, brown_noise.astype(np.float32))

plt.show()