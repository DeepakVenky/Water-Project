
"""
Created on Thu Aug  9 15:36:45 2018

@author: Iswarya
"""
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
 
file = r'F:/WaterCsv/BAK_NEW.xlsx'
df = pd.read_excel(file,header=None)

# =============================================================================
ns=df.loc[df[0]=='[JUNCTIONS]'].index[0]
ne=df.loc[df[0]=='[RESERVOIRS]'].index[0]
# 
l=[]
for i in range(ns+1,ne):
    if isinstance(df.iloc[i][1], (int, float, complex)):
        l.append(df.iloc[i][1])

mydf2 = pd.DataFrame(
    {'Id': l
    })
#print(mydf2)
# #writer = pd.ExcelWriter('C:/Users/Iswarya/Documents/test.xlsx')
#mydf2.to_csv('F:/WaterCsv/bak_nodes.csv')
# 
# 
xs=df.loc[df[0]=='[COORDINATES]'].index[0]
xe=df.loc[df[0]=='[VERTICES]'].index[0]
# 
n=[]
x=[]
y=[]
# 
for i in range(xs+1,xe-1):
    if isinstance(df.iloc[i][1], (int, float, complex)):
        n.append(df.iloc[i][1])
        x.append(df.iloc[i][2])
        y.append(df.iloc[i][3])
print(n)
print(x)
print(y)
mydf3 = pd.DataFrame(
    {'Id': n,
     'latitude': x,
     'longitude': y
    })
print(mydf3)
# #writer = pd.ExcelWriter('C:/Users/Iswarya/Documents/test.xlsx')
#mydf3.to_csv('F:/WaterCsv/bak_coords.csv')
# =============================================================================

es=df.loc[df[0]=='[PIPES]'].index[0]
ee=df.loc[df[0]=='[PUMPS]'].index[0]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(es+1,ee):
    if isinstance(df.iloc[i][1], (int, float, complex)):
        l1.append(df.iloc[i][1])
        l2.append(df.iloc[i][2])
        l3.append(df.iloc[i][3])
        l4.append(df.iloc[i][4])
mydf1 = pd.DataFrame(
    {'Id': l1,
     'Source': l2,
     'Target': l3,
     'Weight':l4
    })
print(mydf1)
#mydf1.drop('Id')
#writer = pd.ExcelWriter('C:/Users/Iswarya/Documents/test.xlsx')
mydf1.to_csv('F:/WaterCsv/bak_pipeLength.csv')

