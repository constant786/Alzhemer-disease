import numpy as np
import matplotlib.pyplot as plt 


n= 500
h=1
k=0.08
a=0.001
r=0.02
b=0.00002

t=[0]
R=[1000]
W=[40]

for i in range(1,n+1):
    t.append(t[i-1]+h)
    R_next=R[i-1] + (k*R[i-1] -a*R[i-1]*W[i-1])*h
    W_next=W[i-1]+ ((-r*W[i-1]) + (b*R[i-1]*W[i-1]))*h
    R.append(R_next)
    W.append(W_next)

plt.figure(figsize=(12,5))
plt.plot(t,R,label="Rabbit",color="blue")
plt.plot(t,W,label="Wolfs",color="orange")
plt.xlabel("time")
plt.ylabel("Nub of Animali")
plt.title("Lotka _Voterra Method ")
plt.legend()
plt.grid(True)
plt.show()



