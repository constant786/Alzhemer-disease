import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k1 = float(input("Value of k1:"))    # aggregation rate (S1 + S2)
k2 = float(input("Value of k2:"))    # nucleation rate (S1^2)
ds = float(input("Value of ds:"))     # microglial clearance of S1
es = float(input("Value of es:"))      # CSF efflux of S1
df = float(input("Value of df:"))    # microglial clearance of S2
n = float(input("Value of n:"))        # microglial density

# Circadian rhythm: production rate r(t)
rw = float(input("Value of rw:"))     # rate during wake
rs = float(input("Value of rs:"))      # rate during sleep
T = float(input("Value of T:"))         # circadian period (hours)

def r(t):
    # Cosine wave: peaks at t=0, trough at t=12
    return (rw + rs)/2 + (rw - rs)/2 * np.cos(2 * np.pi * t / T)

# ODE system
def abeta_odes(t, y):
    S1, S2 = y
    r_t = r(t)
    
    dS1dt = r_t - k1 * S1 * S2 - k2 * S1**2 - (ds * n + es) * S1
    dS2dt = k1 * S1 * S2 + k2 * S1**2 - df * n * S2
    
    return [dS1dt, dS2dt]

# Initial conditions: small amount of Aβ
S1_0 = 0.05
S2_0 = 0.01
y0 = [S1_0, S2_0]

# Time span
t_span = (0, 240)  # simulate for 10 days
t_eval = np.linspace(*t_span, 1000)

# Solve the system
sol = solve_ivp(abeta_odes, t_span, y0, t_eval=t_eval)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='Soluble Aβ (S₁)', linewidth=2)
plt.plot(sol.t, sol.y[1], label='Fibrillar Aβ (S₂)', linewidth=2)
plt.xlabel('Time (hours)')
plt.ylabel('Concentration')
plt.title('Aβ Dynamics with Circadian Production')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
