import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Given data 
Vin = 0.36
k1 = 0.02
kp = 6
Km = 12

def model(y, t):
    G, A = y
    dGdt = Vin - (k1*G*A)
    dAdt = 2*k1*G*A -  (kp * A )/ (Km + A)
    return [dGdt, dAdt]

#  G=3, A=4
y0 = [3, 4]


t = np.linspace(0, 500, 1000)

sol = odeint(model, y0, t)
G_sol = sol[:, 0]
A_sol = sol[:, 1]


plt.plot(t, G_sol, label='Glucose')
plt.plot(t, A_sol, label='ATP')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.title("Glucose and ATP in Yeast Cell")
plt.grid(True)
plt.show()
