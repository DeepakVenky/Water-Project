# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:19:15 2018

@author: Deepak
"""

import seaborn as sn
import pickle
import matplotlib.pylab as plt
import wntr
import pandas as pd
import numpy as np
import datetime 
import math
from matplotlib import animation



inp_file1 = 'F:/WNTR-master/WNTR-master/examples/networks/Net2.inp'
wn1 = wntr.network.WaterNetworkModel(inp_file1)
# =============================================================================
# 
# inp_file2 = 'F:/WNTR-master/WNTR-master/networks/Net2_9_leak.inp'
# wn2 = wntr.network.WaterNetworkModel(inp_file2)
# 
# inp_file3 = 'F:/WNTR-master/WNTR-master/networks/Net2_21_leak.inp'
# wn3 = wntr.network.WaterNetworkModel(inp_file3)
# 
# inp_file4 = 'F:/WNTR-master/WNTR-master/networks/Net2_31_leak.inp'
# wn4 = wntr.network.WaterNetworkModel(inp_file4)
# 
# inp_file5 = 'F:/WNTR-master/WNTR-master/networks/Net2_32_leak.inp'
# wn5 = wntr.network.WaterNetworkModel(inp_file5)
# 
# =============================================================================

epanet_sim1 = wntr.sim.EpanetSimulator(wn1)
epanet_sim_results1 = epanet_sim1.run_sim()
# =============================================================================
# 
# epanet_sim2 = wntr.sim.EpanetSimulator(wn2)
# epanet_sim_results2 = epanet_sim2.run_sim()
# 
# epanet_sim3 = wntr.sim.EpanetSimulator(wn3)
# epanet_sim_results3 = epanet_sim3.run_sim()
# 
# epanet_sim4= wntr.sim.EpanetSimulator(wn4)
# epanet_sim_results4 = epanet_sim4.run_sim()
# 
# epanet_sim5 = wntr.sim.EpanetSimulator(wn5)
# epanet_sim_results5= epanet_sim5.run_sim()
# 
# =============================================================================

mat1=[]
mat2=[]
mat3=[]
mat4=[]
mat5=[]

y1=epanet_sim_results1.link['flowrate']
y2=epanet_sim_results2.link['flowrate']
y3=epanet_sim_results3.link['flowrate']
y4=epanet_sim_results4.link['flowrate']
y5=epanet_sim_results5.link['flowrate']

print(y1)
print(y2)
print(y3)
print(y4)
print(y5)

for i in range(56):
    mat1.append(y1.iloc[i,:])
    
for i in range(56):
    mat2.append(y2.iloc[i,:])
    
for i in range(56):
    mat3.append(y3.iloc[i,:])

for i in range(56):
    mat4.append(y4.iloc[i,:])

for i in range(56):
    mat5.append(y5.iloc[i,:])


print(mat1)

dif1=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(abs((mat2[j][i]*15850.372483753)-(mat1[j][i]*15850.372483753)))
    dif1.append(r)
    
#print(dif1)


dif2=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(abs((mat3[j][i]*15850.372483753)-(mat1[j][i]*15850.372483753)))
    dif2.append(r)
    
#print(dif2)


dif3=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(abs((mat4[j][i]*15850.372483753)-(mat1[j][i]*15850.372483753)))
    dif3.append(r)
    
#print(dif3)

dif4=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(abs((mat5[j][i]*15850.372483753)-(mat1[j][i]*15850.372483753)))
    dif4.append(r)
    
#print(dif4)

dif=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(dif1[i][j]+dif2[i][j]+dif3[i][j]+dif4[i][j])
    dif.append(r)
    

# # #print(dif)
# # # =============================================================================
# # # 
matri=np.matrix(dif)
# # # 
df_cm = pd.DataFrame(matri)
plt.figure(figsize = (55,40))
sn.heatmap(df_cm, annot=True)
plt.savefig('D:\\mat.png')

