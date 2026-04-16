'''
Q3. 
(26%) If the beat wave is defined as:

    x(t)=Acos(2πf_1 t)⋅cos(2πf_2 t)

where the amplitude A = 3, the frequencies f1 = 10Hz and f2 = 200Hz, use a Python program to implement it. 

With a display time t = 0～0.2 seconds and a sampling frequency of fs = 5000Hz, draw the waveform of the beat wave as follows:

(12%) Draw the overlapping two-string waveforms on the same graph and label each wave function

(7%) Draw the waveform of the beat wave

(7%) Plot the envelope phenomenon of the beat wave, that is, overlay the low-frequency signal waveform with the beat wave waveform.
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

plt.plot(t, x1)
plt.plot(t, x2)
plt.legend
plt.grid(True)
plt.show

plt.plot(t, x)
plt.grid(True)
plt.show()