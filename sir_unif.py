import matplotlib.pyplot as plt
import numpy as np

def SIRfunction(beta, gamma, N, I0, T, NT):
    s = N - I0
    I = I0
    R = 0
    dt = T/NT
    S = np.hstack([[s], np.zeros(NT)])
    I = np.hstack([[I0], np.zeros(NT)])
    R = np.zeros(NT + 1)
    for n in range(NT):
        S[n + 1] = S[n] + dt*(-beta*I[n]*S[n]/N) 
        I[n + 1] = I[n] + dt*(beta*I[n]*S[n]/N - gamma*I[n])
        R[n + 1] = R[n] + dt*(gamma*I[n])
    return S, I, R

def randombeta(beta,dev,anzahl):
    rng = np.random.default_rng()
    B = rng.normal(beta, dev, anzahl)
    return B

def randomgamma(gamma,dev,anzahl):
    rng = np.random.default_rng()
    G = rng.normal(gamma, dev, anzahl)
    return G

def UQ(beta, gamma, N, I0, T, NT, dev1, dev2, anzahl):
    
    rb = randombeta(beta,dev1,anzahl)
    rg = randomgamma(gamma,dev2,anzahl)
    
    SW = np.array([])
    IW = np.array([])
    RW = np.array([])
    
    for i in range(len(rb)):
        s,i,r = SIRfunction(rb[i], rg[i], N, I0, T, NT)
        if len(SW) == 0:
            SW = np.array([s])
            IW = np.array([i])
            RW = np.array([r])
        else:
            SW = np.vstack([SW, s])
            IW = np.vstack([IW, i])
            RW = np.vstack([RW, r])
            
    Savg = np.sum(SW, axis=0) / anzahl
    Iavg = np.sum(IW, axis=0) / anzahl
    Ravg = np.sum(RW, axis=0) / anzahl
    
    listmax = [np.array([]),np.array([]),np.array([])]
    listmin = [np.array([]),np.array([]),np.array([])]
    listat = [SW, IW, RW]
    
    for x in range(3):
        subst = np.array([])
        for i in range(len(s)):
            maxEin = 0
            for j in range(len(rb)):
                if listat[x][j,i] > maxEin:
                    maxEin = listat[x][j,i]
            subst = np.hstack([subst, [maxEin]])
            listmax[x] = subst
            
    for x in range(3):
        subst = np.array([])
        for i in range(len(s)):
            minEin = N
            for j in range(len(rb)):
                if listat[x][j,i] < minEin:
                    minEin = listat[x][j,i]
            subst = np.hstack([subst, [minEin]])
            listmin[x] = subst
            
    return Savg, Iavg, Ravg, listmax[0], listmax[1], listmax[2], listmin[0], listmin[1], listmin[2]




Sav, Iav, Rav, yerrmaxS, yerrmaxI, yerrmaxR, yerrminS, yerrminI, yerrminR = UQ(0.2, 0.05, 8*10**7, 1, 730, 1000, 0.02, 0.005, 10)




y_errorS = [abs(Sav - yerrminS), abs(Sav - yerrmaxS)]
y_errorI = [abs(Iav - yerrminI), abs(Iav - yerrmaxI)]
y_errorR = [abs(Rav - yerrminR), abs(Rav - yerrmaxR)]


plt.title("SIRModell mit zufälligen Parametern und Error")
plt.xlabel("Zeitpunkte t")
plt.ylabel("Gesamtbevölkerung N")

plt.errorbar(range(len(Sav)), Sav, yerr = y_errorS, fmt ='-o')
plt.errorbar(range(len(Rav)), Rav, yerr = y_errorR, fmt ='-o')

plt.errorbar(range(len(Iav)), Iav, yerr = y_errorI, fmt ='-o')

plt.show()

