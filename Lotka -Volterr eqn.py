import numpy as np
import matplotlib.pyplot as plt 


n=555   # no of itteration  , any thing from mind
h=1
k=0.08
a=0.001
r=0.02
b=0.00002

t = [0]
R = [int(input("No of initial Prey: "))]
W = [int(input("No of initial Predator: "))]


for i in range(1,n+1):
    t.append(t[i-1]+h)
    R_next=R[i-1] + (k*R[i-1] -a*R[i-1]*W[i-1])*h
    W_next=W[i-1]+ ((-r*W[i-1]) + (b*R[i-1]*W[i-1]))*h
    R.append(R_next)
    W.append(W_next)

plt.figure(figsize=(12,5))
plt.plot(t,R,label="Rabbit",color="blue")
plt.plot(t,W,label="Wolfs",color="orange")
plt.xlabel("Time")
plt.ylabel("Number of Animal")
plt.title("Lotka _Voterra Method ")
plt.legend()
plt.grid(True)
plt.show()



