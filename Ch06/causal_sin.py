# prompt: generate a causal system with sin signal

import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 10, 500)

# Input signal (sinusoidal)
x = np.sin(2 * np.pi * 0.5 * t)  # Frequency = 0.5 Hz

# Define the system parameters (example: a simple first-order system)
a = -0.8  # System parameter

# Initialize the output signal
y = np.zeros_like(x)

# Simulate the system (discrete-time system using Euler's method)
for i in range(2, len(t)):
    y[i] = a * y[i-1] + 1/3*(x[i-2]+x[i-1]+x[i]) # Example: First order system

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Input (x)')
plt.plot(t, y, label='Output (y)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Causal System Response to Sinusoidal Input')
plt.legend()
plt.grid(True)
plt.show()
