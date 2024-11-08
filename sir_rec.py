import numpy as np
import matplotlib.pyplot as plt

# 

def SIR_recovery(beta, gamma, N, I0, mortality_rate, T):
    s = N - I0
    total_deaths = 0
    recovery = np.zeros(90)
    infections = np.zeros(14)
    infections[0] = I0
    S = np.hstack([s, np.zeros(T)])
    I = np.hstack([[I0], np.zeros(T)])
    R = np.zeros(T + 1)
    TD = np.zeros(T + 1)
    DD = np.zeros(T + 1)
    for n in range(T):
        I[n + 1] = np.sum(infections)
        day_infections = beta*(((I[n]*S[n])/N) - gamma*I[n])
        infections[1:] = infections[:-1]
        infections[0] = day_infections
        DD[n + 1] = infections[-1] * mortality_rate
        TD[n + 1] = TD[n] + DD[n + 1]
        S[n + 1] = N - np.sum(infections) - np.sum(recovery)
        day_recoveries = infections[-1] - DD[n + 1]
        recovery[1:] = recovery[:-1]
        recovery[0] = day_recoveries
        R[n + 1] = np.sum(recovery)
        N = N - DD[n + 1]
        
                
    plt.plot(S)
    plt.plot(I)
    plt.plot(R)
    plt.plot(TD)
    plt.plot(DD)
    plt.show()
    

        
SIR_recovery(0.2, 0.05,80000000,1,0.1,730)