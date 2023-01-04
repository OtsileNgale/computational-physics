import numpy as np
from numpy import linspace, sin, exp, pi, cos, sqrt
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
from pandas import Series, DataFrame
import argparse
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib.ticker import NullFormatter
import sys
import pylab
import math

#Thermal physics
#Code for temperature vs multiplicity

NA = 100
NB = 300
x = 2+7+7+0+4+8+1+5
q = x
N = NA +NB

omega_A = [None]*(q + 1)   #multiplicities of A
q_A = [None]*(q + 1)  #macrostates of A
omega_B = [None]*(q + 1)
q_B = [None]*(q + 1)
omega_total = [None]*(q + 1)
E_total = [None]*(q + 1)     #Total Entropy
E_A = [None]*(q + 1)     #Entropies of A
E_B = [None]*(q + 1)
T_A = [None]*(q + 1)     #Temperature of A
T_B = [None]*(q + 1)     #Temperature of B

for i in range(0, q + 1):
    qA = i
    
    q_A[i] = qA
    omega_A[i] = math.factorial(q_A[i] + NA - 1)/(math.factorial(q_A[i])*math.factorial(NA - 1))
    E_A[i] = math.log(omega_A[i])
    
    qB = q - qA
    q_B[i] = qB
    omega_B[i] = math.factorial(q_B[i] + NB -1)/(math.factorial(q_B[i])*math.factorial(NB - 1))
    E_B[i] = math.log(omega_B[i])
    
    omega_total[i] = np.multiply(omega_A[i], omega_B[i])
    E_total[i] = math.log(omega_total[i])
    
for i in range(0, q - 1):
    T_A[i] = (q_A[i + 2] - q_A[i])/(E_A[i + 2] - E_A[i])
    T_B[i] = (q_B[i + 2] - q_B[i])/(E_B[i + 2] - E_B[i])
    

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)
    
plt.plot(q_A, T_A)
plt.plot(q_B, T_B)
plt.xlabel('q_A')
plt.ylabel('Temperature(K)')
plt.title('Temperature vs q_A')
plt.plot(T_A, color = 'pink', label = 'T_A')
plt.plot(T_B, color = 'yellow', label = 'T_B')
plt.grid()
ax.text(20, 0.5, 'Ngale, O.R 27704815', style = 'italic' )
ax.text(0, 0.85, 'NA = 100,NB = 300', style = 'italic' )

location = 0
legend_draw_flag = True
plt.legend()

T = [q_A, omega_A, E_A, q_B, omega_B, E_B, omega_total, E_total]
#print(T)
df = pd.DataFrame(list(zip(q_A, omega_A, E_A, q_B, omega_B, E_B, omega_total, E_total)), columns = ['q_A values', 'Omega_A values', 'Entropy of A',
                                                                                                   'q_B values', 'Omega_B values', 'Entropy of B', 
                                                                                                   'Omega_total', 'Total Entropy'])
print(df)

    