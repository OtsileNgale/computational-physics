import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
########################################################################################################################
studnums = "27704815"        
date     = "2022/2/11"  
expnum   = "2"
xlabel   = "name of X (units)"
ylabel   = "name of Y (units)"
expname  = "H-R Diagram"
aratio   = 210/297. #aspect ratio of your canvas
################################################################################################################################
title = expname
filename = 'plot1'

################################################################################################################################

a2 = '10e5.txt'
a1 = '1.0e61.txt'
a3 = '1.0e7.txt'
a4 = '1.0e8.txt'
a5 = '1.0e9.txt'
a6 = '1.0e10.txt'


df1 = pd.read_csv(a1, sep='\s+', names=['Vmag','Bmag'])
df2 = pd.read_csv(a2, sep='\s+', names=['Vmag','Bmag'])
df3 = pd.read_csv(a3, sep='\s+', names=['Vmag','Bmag'])
df4 = pd.read_csv(a4, sep='\s+', names=['Vmag','Bmag'])
df5 = pd.read_csv(a5, sep='\s+', names=['Vmag','Bmag'])
df6 = pd.read_csv(a6, sep='\s+', names=['Vmag','Bmag'])
################################################################################################################################

V1 = df1["Vmag"]
BV1 = df1["Bmag"] - df1["Vmag"]
#print(BV1)
#print(V1)
#figure out smart limits in X
Xrange = np.max(BV1) - np.min(BV1)
xmin = np.min(BV1) - 0.03 * Xrange
xmax = np.max(BV1) + 0.03 * Xrange

Yrange = np.max(V1) - np.min(V1)
ymin = np.min(V1) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V1) + 0.1 * Yrange

V2 = df2["Vmag"]
BV2 = df2["Bmag"] - df2["Vmag"]
#print(BV2)
#print(V2)
#figure out smart limits in X
Xrange = np.max(BV2) - np.min(BV2)
xmin = np.min(BV2) - 0.03 * Xrange
xmax = np.max(BV2) + 0.03 * Xrange

Yrange = np.max(V2) - np.min(V2)
ymin = np.min(V2) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V2) + 0.1 * Yrange

V3 = df3["Vmag"]
BV3 = df3["Bmag"] - df3["Vmag"]
#print(BV1=3)
#print(V3)
#figure out smart limits in X
Xrange = np.max(BV3) - np.min(BV3)
xmin = np.min(BV3) - 0.03 * Xrange
xmax = np.max(BV3) + 0.03 * Xrange

Yrange = np.max(V3) - np.min(V3)
ymin = np.min(V3) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V3) + 0.1 * Yrange

V4 = df4["Vmag"]
BV4 = df4["Bmag"] - df4["Vmag"]
#print(BV4)
#print(V4)
#figure out smart limits in X
Xrange = np.max(BV4) - np.min(BV4)
xmin = np.min(BV4) - 0.03 * Xrange
xmax = np.max(BV4) + 0.03 * Xrange

Yrange = np.max(V4) - np.min(V4)
ymin = np.min(V4) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V4) + 0.1 * Yrange

V5 = df5["Vmag"]
BV5 = df5["Bmag"] - df5["Vmag"]
#print(BV5)
#print(V5)
#figure out smart limits in X
Xrange = np.max(BV5) - np.min(BV5)
xmin = np.min(BV5) - 0.03 * Xrange
xmax = np.max(BV5) + 0.03 * Xrange

Yrange = np.max(V5) - np.min(V5)
ymin = np.min(V5) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V5) + 0.1 * Yrange

V6 = df6["Vmag"]
BV6 = df6["Bmag"] - df6["Vmag"]
#print(BV6)
#print(V6)
#figure out smart limits in X
Xrange = np.max(BV6) - np.min(BV6)
xmin = np.min(BV6) - 0.03 * Xrange
xmax = np.max(BV6) + 0.03 * Xrange

Yrange = np.max(V6) - np.min(V6)
ymin = np.min(V6) - 0.2 * Yrange # larger space for info at bottom
ymax = np.max(V6) + 0.1 * Yrange

################################################################################################################################

fig = plt.figure(figsize=(10,10*aratio)) #Figure canvas size. 10 x ?? is good 
fig.set_tight_layout(True) #Useful to get rid of extra white space borders

plt.plot(BV1, V1, 'r')
plt.plot(BV2, V2, 'b')