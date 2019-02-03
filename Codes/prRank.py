# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 08:57:37 2018

@author: Iswarya
"""
import pandas as pd
df1=pd.read_csv('C:/Users/Iswarya/Documents/Pressure_Diff17-BLA.csv')
##print(df1['# Result'])
##leaknode=df1['# Result'][9]
##print(leaknode)

df1['Weight'] = df1['# Result'].map(lambda x: abs(x))
###print(df1['Weight'])

##df1['rank'] = df1.sort_values(['Weight'])['Weight'].index + 1

'''
for index,row in df1.iterrows():
    if row['# Result']<leaknode:
        print('NEG')
        print(row['Weight'])
        row['Weight']=row['Weight']*-1
        print(row['Weight'])
        df1.at[index,'Weight']=row['Weight']
print(df1.Weight)
'''
df1.to_csv('C:/Users/Iswarya/Documents/Pressure_Diff17-BLA-rank-2.csv')

