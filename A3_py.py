# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:08:55 2021

@author: MSI-PC
"""

import numpy as np

import math

from scipy.stats import norm
from scipy.stats import t

import matplotlib.pyplot as plt
from scipy.stats import binom
from statistics import stdev

# range for floats with np.arange()
#for muRange in np.arange(51, 55, 0.02):
    #print(muRange, end=', ')
n = 20
N = 5000
mu0 = 53.0
powerT, powerU = [], []
muRange = np.arange(51,55,0.02)

'''
def myFunc(m):
  if m < 53:
    return False
  else:
    return True
'''
for muActual in muRange:
    dist=norm(muActual, 1.2)
    rejectT, rejectU = 0, 0
    np.random.seed(1)

    for _ in range(1, N):
        data = dist.rvs(20)
        xBar = np.mean(data)
        stdDev = stdev(data)
        
        tStatT = (xBar - mu0)/(stdDev/math.sqrt(n))
        
        #tdist=np.random.standard_t(_,size=(n-1))
        t_dist = t(n-1)
        #pValT=jax.scipy.stats.t.pdf(abs(tStatT))
        pValT = 2*t_dist.pdf(abs(tStatT))
        
        #data1=(data>53.0)

        #data1=list(filter(myFunc,data))
        #xPositive = len(data1)
        xPositive =sum(data>53)
        uStat = max(xPositive, n-xPositive)
        #bino = st.binom(n,0.5)
        ber_dist=binom(n,0.5)
        pValSign = 2*ber_dist.pmf(uStat)
        
        rejectT += pValT <0.05
        rejectU += pValSign  <0.05
    powerT.append(rejectT/N)
    powerU.append(rejectU/N)
plt.plot(muRange,powerT,"-b",label="t test")
plt.plot(muRange,powerU,"-r",label="sign test")
plt.legend(loc="upper left")
plt.show()

