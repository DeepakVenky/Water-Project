# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:27:39 2018

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
import toyplot as tp

inp_file1 = 'networks/Net2.inp'
wn1 = wntr.network.WaterNetworkModel(inp_file1)


#sim = wntr.sim.WNTRSimulator(wn,mode='PDD')
#results = sim.run_sim(solver_options={}, convergence_error=True)


epanet_sim = wntr.sim.EpanetSimulator(wn1)
epanet_sim_results = epanet_sim.run_sim()

#print(epanet_sim_results.link['flowrate'])
#print(epanet_sim_results.node['demand'])
y=epanet_sim_results.link['flowrate']
#contains flow rates across all times for all pipes (0 to 55 hrs)
mat=[]

#print(y.iloc[55,:])

for i in range(56):
    mat.append(y.iloc[i,:])
    
#print(mat[0])


inp_file2 = 'networks/Net2_9_leak.inp'
wn2 = wntr.network.WaterNetworkModel(inp_file2)



epanet_sim = wntr.sim.EpanetSimulator(wn2)
epanet_sim_results = epanet_sim.run_sim()

z=epanet_sim_results.link['flowrate']

mat1=[]

for i in range(56):
    mat1.append(z.iloc[i,:])
    
#print(mat1[0])
#t=list(mat1[0].index)
print(list(mat1[0].index))
#dif1=[]
#for i in range(42):
 #   dif1.append(mat1[i]-mat[i])

#15850.372483753
dif=[]

for i in range(40):
    r=[]
    for j in range(56):
        r.append(abs((mat1[j][i]*15850.372483753)-(mat[j][i]*15850.372483753)))
    dif.append(r)
    
#print(dif)


matri=np.matrix(dif)
m=matri.transpose()
 
#print(pd.DataFrame(matri))

t=[]

for i in range(56):
    t.append(list(mat1[0].index))

r=np.array(t)    

df_cm = pd.DataFrame(m)
plt.figure(figsize = (55,40))
sn.heatmap(df_cm, annot=r,fmt='')
#plt.savefig('D:\\mat9.png')


