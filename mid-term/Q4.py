'''
Q4. 
(12%) With a sampling frequency of fs = 1500Hz and a signal phase shift of 0, between 0 and 2 seconds of display time, 
    use the SciPy Signal library in Python to generate a chirp signal (up-chirp), 
    where the chirp signal frequency ranges from 1Hz to 350Hz in a non-linear logarithmic scan, 
    with the initial and final frequencies at time points of 0 and 3 seconds respectively, 
    and display its waveform.
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