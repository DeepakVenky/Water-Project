
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

inp_file1 = 'networks/3_Foss_poly_1.inp'
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

for i in range(49):
    mat.append(y.iloc[i,:])
    
print(mat[0])


inp_file2 = 'networks/3_Foss_poly_1leak22.inp'
wn2 = wntr.network.WaterNetworkModel(inp_file2)



epanet_sim = wntr.sim.EpanetSimulator(wn2)
epanet_sim_results = epanet_sim.run_sim()

z=epanet_sim_results.link['flowrate']

mat1=[]
print("vghcfyhfc")
for i in range(49):
    mat1.append(z.iloc[i,:])
    

#t=list(mat1[0].index)
#print(list(mat1[0].index))
#dif1=[]
#for i in range(42):
 #   dif1.append(mat1[i]-mat[i])

#15850.372483753
dif=[]

for i in range(57):
    r=[]
    for j in range(49):
        r.append(abs((mat1[j][i]*15850.372483753)-(mat[j][i]*15850.372483753)))
    dif.append(r)
    
#print(dif)


matri=np.matrix(dif)
m=matri.transpose()
 
#print(pd.DataFrame(matri))

t=[]

for i in range(49):
    t.append(list(mat1[0].index))

r=np.array(t)    

df_cm = pd.DataFrame(m)
plt.figure(figsize = (48,57))
sn.heatmap(df_cm, annot=True)
plt.savefig('D:\\matfoss22transpose.png')



