'''
Q1. (30%) 
If the general exponential sine wave is defined as:

    x(t)=A[cos(ωt+ϕ)+jsin(ωt+ϕ)]

Assume the parameters forming two sine waves are: amplitude (A), angular frequency (ω), and phase shift (ϕ) respectively:

    A: 12, 16, ω: 4π, 8π, ϕ: π/4, 3π/4

Based on the above parameters of the two sine waves,
    use a Python program to implement the synthesis of a harmonic wave by summing the two sine waves and sampling at a frequency of fs = 200Hz between 0 and 2 seconds:

    x(t)=x_1(t)+x_2(t)

(12%) Draw the waveforms of the two overlapping sine waves on the same graph and label each wave function on the graph.

(8%) Draw the synthesized harmonic waveform.

(10%) Explain the relationship between the frequency of the harmonic wave and the two sine waves.
'''

import numpy as np
import matplotlib.pyplot as plt

# ===========================================================================================================

# Sampling parameters
sampl_freq = 200 
time_window = [0, 2]

# Time array
t = np.linspace(time_window[0], time_window[1], sampl_freq)

# Sine wave parameters
x1_para = [12, 4 * np.pi, np.pi /4]
x2_para = [16, 8 * np.pi, 3 * np.pi / 4]

# ===========================================================================================================

# Wave synthesizing
def wave_synthesis(parameter):
    A = parameter[0]
    w = parameter[1]
    phi = parameter[2]

    # Apply: x(t)=A[cos(ωt+ϕ)+jsin(ωt+ϕ)]
    x = A * (np.cos(w * t + phi) + 1j * np.sin(w * t + phi))
    
    return x

# Wave summing
def wave_summing(*component_waves):
    x = 0 * component_waves[0]
    for wave in component_waves:
        x += wave

    return x

# ===========================================================================================================
    
x1 = wave_synthesis(x1_para)
x2 = wave_synthesis(x2_para)
x = wave_summing(x1, x2)

# ===========================================================================================================

# (12%) Draw the waveforms of the two overlapping sine waves on the same graph and label each wave function on the graph.
# Ans:
plt.plot(t, x1)
plt.plot(t, x2)
plt.grid(True)
plt.legend(['x_1(t)', 'x_2(t)'])
plt.show()

# (8%) Draw the synthesized harmonic waveform.
# Ans:
plt.plot(t, x)
plt.grid(True)
plt.show()