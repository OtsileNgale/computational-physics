import numpy as np
import matplotlib.pyplot as plt
import math

#Thermal Physics
#This is a code to plot the entroy vs multiplicity graph in Thermodynamics

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

N1 = 100
N2 = 100

x = 2+7+7+0+4+8+1+5
print(x)

q_total = []
for i in range(0,x, 1):
    q_total.append(i)
    #print(q_total)
    
q_A = []
for i in range(0, x, 1):
    q_A.append(i)
    #print(q_A)
    
omega_A = []
lnOmega_A = []
for i in q_A:
    A = (math.factorial(i + N1 - 1 ))/(math.factorial(i)*math.factorial(N1 - 1))
    A1 = math.log(A)
    omega_A.append(A)
    lnOmega_A.append(A1)
    #print(omega_A)
    #print(lnOmega_A)
    
q_B = []
for i in range(0, x, 1):
    q_B.append(i)
    reversed_qB = list(reversed(q_B))
    #print(q_B)
    #print(reversed_qB)
    
omega_B = []
lnOmega_B = []
for i in reversed_qB:
    B = (math.factorial(i + N2 -1))/(math.factorial(i)*math.factorial(N2 - 1))
    B1 = math.log(B)
    omega_B.append(B)
    lnOmega_B.append(B1)
    #print(omega_B)
    #print(lnOmega_B)
    
omega_total = (np.multiply(omega_A, omega_B))
#print(omega_total)

total = []
lnOmegaTotal = []
for i in omega_total:
    total.append(i)
    lnTotalValues = math.log(i)
    lnOmegaTotal.append(lnTotalValues)
    #print(lnOmegaTotal)
    
plt.plot(lnOmega_A, color = 'blue', label = 'sA/k')
plt.plot(lnOmega_B, color = 'red', label = 'SB/k')
plt.plot(lnOmegaTotal, color = 'green', label = 'STotal/k')
plt.title("The graph of Entropy", fontsize = 19)
plt.xlabel("q_A", fontsize = 15)
plt.ylabel("Entropy(in units of k", fontsize = 15)
ax.text(19, 110, 'Ngale, O.R 27704815', style='italic')
ax.text(0, 112, 'NA = 100,NB = 100', style = 'italic' )
plt.legend()
plt.grid()
plt.show()