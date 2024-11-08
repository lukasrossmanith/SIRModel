import matplotlib.pyplot as plt
import numpy as np


def SIRfunction(beta, gamma, N, I0, T, NT):
    s = N - I0
    I = I0
    R = 0
    dt = T/NT
    S = np.hstack([s, np.zeros(NT)])
    I = np.hstack([I0, np.zeros(NT)])
    R = np.zeros(NT + 1)
    for n in range(NT):
        S[n + 1] = S[n] + dt*(-beta*I[n]*S[n]/N) 
        I[n + 1] = I[n] + dt*(beta*I[n]*S[n]/N - gamma*I[n])
        R[n + 1] = R[n] + dt*(gamma*I[n])
    
    plt.plot(S)
    plt.plot(I)
    plt.plot(R)
    plt.axis((0, NT, 0, N + 1))
    plt.show()

SIRfunction(0.2, 0.05, 8*10**7, 1, 730, 1000)



