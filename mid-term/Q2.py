'''
Q2. (20%) Continuing from Q1's harmonic wave, calculate the parameters of the two sine waves and the harmonic:

(8%)  Calculate the phasors X̃1 and X̃2 of the two sine waves respectively.
(12%) Calculate the phasor X̃ of the harmonic wave, its amplitude and phase shift.
'''

import numpy as np

# ===========================================================================================================

# Parameters (same as Q1)
x1_para = [12, 4 * np.pi, np.pi / 4]   # A1, ω1, ϕ1
x2_para = [16, 8 * np.pi, 3 * np.pi / 4]  # A2, ω2, ϕ2

# ===========================================================================================================

# (8%) Calculate the phasors X̃1 and X̃2 of the two sine waves.
# Ans:
# A phasor is defined as: X̃ = A * e^(jϕ) = A[cos(ϕ) + j·sin(ϕ)]
# (It captures amplitude and phase; angular frequency ω is implicit.)

A1, w1, phi1 = x1_para
A2, w2, phi2 = x2_para

X1_phasor = A1 * np.exp(1j * phi1)
X2_phasor = A2 * np.exp(1j * phi2)

print("=== Phasors of the two sine waves ===")
print(f"X̃1 = {A1} · e^(j·π/4)")
print(f"   = {X1_phasor:.4f}")
print(f"   Amplitude : {np.abs(X1_phasor):.4f}")
print(f"   Phase     : {np.angle(X1_phasor):.4f} rad  ({np.degrees(np.angle(X1_phasor)):.2f}°)")
print()
print(f"X̃2 = {A2} · e^(j·3π/4)")
print(f"   = {X2_phasor:.4f}")
print(f"   Amplitude : {np.abs(X2_phasor):.4f}")
print(f"   Phase     : {np.angle(X2_phasor):.4f} rad  ({np.degrees(np.angle(X2_phasor)):.2f}°)")
print()

# ===========================================================================================================

# (12%) Calculate the phasor X̃ of the harmonic wave, its amplitude and phase shift.
# Ans:
# NOTE: x1 and x2 have DIFFERENT angular frequencies (4π vs 8π),
# so they cannot be added as a single phasor in the classical sense.
# However, we can represent the harmonic as a sum of two phasors at their
# respective frequencies:
#
#   x(t) = Re{ X̃1 · e^(jω1t) } + Re{ X̃2 · e^(jω2t) }
#
# The "effective" or resultant phasor is often computed numerically by
# evaluating the complex sum at a reference time t = 0:

X_phasor = X1_phasor + X2_phasor   # vector sum at t = 0

A_harmonic   = np.abs(X_phasor)
phi_harmonic = np.angle(X_phasor)

print("=== Phasor of the harmonic wave (vector sum at t = 0) ===")
print(f"X̃ = X̃1 + X̃2")
print(f"  = {X1_phasor:.4f} + {X2_phasor:.4f}")
print(f"  = {X_phasor:.4f}")
print(f"  Amplitude  A = {A_harmonic:.4f}")
print(f"  Phase shift ϕ = {phi_harmonic:.4f} rad  ({np.degrees(phi_harmonic):.2f}°)")
