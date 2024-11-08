import matplotlib.pyplot as plt
import numpy as np


def SIRfunction(beta, gamma, N, I0, T, NT, e):
    NT = NT/2
    dt = T/NT
    itforep = 0
    ep = None
    SG = np.array([])
    IG = np.array([])
    RG = np.array([])
    while ep == None or ep > e:
        S = N - I0
        I = I0
        R = 0
        itforep += 1
        dt = dt/2
        NT = int(NT*2)
        SG1 = SG
        IG1 = IG
        RG1 = RG
        SG = np.array([])
        IG = np.array([])
        RG = np.array([])
        for i in range(1, NT+1):
            S = S + dt*(-beta*I*S/N) 
            I = I + dt*(beta*I*S/N - gamma*I)
            R = R + dt*(gamma*I)
            SG = np.hstack([SG,[S]])
            IG = np.hstack([IG,[I]])
            RG = np.hstack([RG,[R]])
        if SG1.size > 0:
            SComp = np.zeros(NT//2)
            IComp = np.zeros(NT//2)
            RComp = np.zeros(NT//2)
            for l in range(NT//2):
                SComp[l] = SG[l*2]
                IComp[l] = IG[l*2]
                RComp[l] = RG[l*2] 
            SDif = abs(SG1 - SComp)
            SMax = np.argmax(SDif)
            IDif = abs(IG1 - IComp)
            IMax = np.argmax(IDif)
            RDif = abs(RG1 - RComp)
            RMax = np.argmax(RDif)
            ep = max(SDif[SMax], IDif[IMax], RDif[RMax])
    return itforep

print(SIRfunction(0.2, 0.05, 8*10**7, 1, 730, 100, 1000000))