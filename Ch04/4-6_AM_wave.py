# prompt: plot an AM signal with carrier frequency=20

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 20  # Carrier frequency
fm = 1  # Message frequency
Am = 1  # Message amplitude
Ac = 1  # Carrier amplitude
duration = 1  # Duration of the signal in seconds
fs = 1000  # Sampling frequency

# Generate time values
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate message signal (e.g., a sinusoidal wave)
message_signal = Am * np.cos(2 * np.pi * fm * t)

# Generate carrier signal
carrier_signal = Ac * np.cos(2 * np.pi * fc * t)

# Generate AM signal
am_signal = (1 + message_signal) * carrier_signal

# Plot the signals
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title('AM Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
