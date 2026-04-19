'''
Q4. (12%) Display time 0~2 s, sampling frequency fs = 1500 Hz, signal phase shift = 0.
Use Python's SciPy Signal package to generate an up-chirp signal,
where the chirp frequency sweeps non-linearly (logarithmic) from 1 Hz to 350 Hz.
The initial and final frequencies correspond to t = 0 s and t = 3 s respectively.
Display the waveform.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# ===========================================================================================================

# Parameters
fs = 1500  # Hz
t = np.linspace(0, 2, fs * 2)   # 0 ~ 2 s, 3000 samples
f0 = 1  # Hz  – frequency at t = 0
f1 = 350  # Hz  – frequency at t1 = 3 s
t1 = 3  # s   – reference time for final frequency
phi = 0  # deg – phase shift (scipy chirp uses degrees)

# ===========================================================================================================

# Generate logarithmic up-chirp
x_chirp = chirp(t, f0=f0, f1=f1, t1=t1, method='logarithmic', phi=phi)

# ===========================================================================================================

# Display waveform
plt.figure(figsize=(10, 4))
plt.plot(t, x_chirp, linewidth=0.6, color='darkorange', label='Up-Chirp (logarithmic, 1→350 Hz)')
plt.title('Logarithmic Up-Chirp Signal (0~2 s)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
