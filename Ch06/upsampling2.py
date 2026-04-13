# prompt: generate cos upsampling by 2 with linear interpolation

import numpy as np
import matplotlib.pyplot as plt

def cos_upsample(x, factor):
  """Upsamples a 1D cosine wave by a given factor using linear interpolation.

  Args:
      x: A 1D numpy array representing the cosine wave.
      factor: The upsampling factor.

  Returns:
      A 1D numpy array representing the upsampled cosine wave.
  """

  n = len(x)
  new_n = n * factor
  upsampled_x = np.zeros(new_n)

  for i in range(n - 1):
    # Calculate indices for linear interpolation
    start = i * factor
    end = (i + 1) * factor

    # Generate linearly spaced indices for the upsampled array
    upsampled_indices = np.arange(start, end)

    # Linear interpolation
    upsampled_x[int(start):int(end)] = np.interp(upsampled_indices, [i * factor, (i + 1) * factor], [x[i], x[i+1]])

  #Handle the last point
  upsampled_x[int((n-1)*factor)] = x[n-1]
  return upsampled_x


# Example usage
# Generate a sample cosine wave
x = np.cos(np.linspace(0, 4 * np.pi, 10))

# Upsample by a factor of 2, 4, 8
upsampled_x = cos_upsample(x, 2)

# Print the original and upsampled arrays
print("Original signal:")
print(x)
print("\nUpsampled signal:")
print(upsampled_x)

plt.figure(1)
plt.title('Original Signal')
plt.stem(x, linefmt='b-', markerfmt='ro')

plt.figure(2)
plt.title('Original Signal VS. Upsampled Signal')
plt.stem(x, label='Original Signal', linefmt='b-', markerfmt='bo')
plt.stem(upsampled_x, label='Upsampled Signal', linefmt='r-', markerfmt='ro')
plt.legend()

# prompt: plot cos upsampling by 2 with linear interpolation

plt.figure(3)
plt.plot(x, label='Original Signal')
plt.plot(upsampled_x, label='Upsampled Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Cosine Wave Upsampling')
plt.legend()
plt.grid(True)

# prompt: plot linear interpolation using interp1d

from scipy.interpolate import interp1d

def cos_upsample(x, factor):
  """Upsamples a 1D cosine wave by a given factor using linear interpolation.

  Args:
      x: A 1D numpy array representing the cosine wave.
      factor: The upsampling factor.

  Returns:
      A 1D numpy array representing the upsampled cosine wave.
  """

  #Using interp1d for linear interpolation
  f = interp1d(np.arange(len(x)), x, kind='linear')
  upsampled_x = f(np.linspace(0, len(x)-1, len(x)*factor))
  return upsampled_x

# Example usage
# Generate a sample cosine wave
x = np.cos(np.linspace(0, 4 * np.pi, 10))

# Upsample by a factor of 2
upsampled_x = cos_upsample(x, 2)

# Print the original and upsampled arrays
print("Original signal:")
print(x)
print("\nUpsampled signal:")
print(upsampled_x)

# Plotting
plt.figure(4)
plt.plot(x, label='Original Signal', marker='o', linestyle='-')
plt.plot(upsampled_x, label='Upsampled Signal', marker='x', linestyle='--')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Cosine Wave Upsampling using interp1d')
plt.legend()
plt.grid(True)
plt.show()