import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def model(t, y, n, s, k12, k21, k34, k43):
  
    X1, X2, X3 = y

    dX1_dt = n * (-k12 * X1**n + k21 * X2)

    dX2_dt = s * (-k34 * X2**s + k43 * X1**n) + k12 * X1**n - k21 * X2

    dX3_dt = k34 * X2**s - k43 * X3

    return [dX1_dt, dX2_dt, dX3_dt]

n = float(input("Put Value of n: "))
s = float(input("Input Value of s: "))

k12 =float(input("Input Value of k12:"))
k21 = float(input("Input Value of k21:"))
k34 =float(input("Input Value of k34:"))
k43 = float(input("Input Value of k43:"))

# --- Define the initial state of the system ---
# Initial values for [X1, X2, X3] at time t=0
y0 = [1.0, 0.0, 0.0]  # Start with only X1 present

# --- Define the time span for the simulation ---
t_span = (0, 100) # Simulate from t=0 to t=100
t_eval = np.linspace(t_span[0], t_span[1], 500) 

params = (n, s, k12, k21, k34, k43)

# Call the ODE solver
solution = solve_ivp(fun=model, t_span=t_span, y0=y0, args=params, t_eval=t_eval)

# 4. Visualize the results
# plt.style.use('seaborn-v0_8-whitegrid')
# plt.figure(figsize=(10, 6))

# Plot each variable over time
plt.plot(solution.t, solution.y[0], label='$X_1(t)$')
plt.plot(solution.t, solution.y[1], label='$X_2(t)$')
plt.plot(solution.t, solution.y[2], label='$X_3(t)$')

# Add labels and title for clarity
plt.title('Nucleation-dependent Model')
plt.xlabel('Time (t)')
plt.ylabel('Concentration')
plt.legend()
plt.grid(True)
plt.show()