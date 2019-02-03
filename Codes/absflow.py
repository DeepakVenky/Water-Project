# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 08:57:37 2018

@author: Iswarya
"""
import pandas as pd
df1=pd.read_csv('C:/Users/Iswarya/Documents/Bal_FlowDiffTotal.csv')
print(df1.Weight)
for index,row in df1.iterrows():
    if row['Weight']<0:
        print('NEG')
        print(row['Weight'])
        row['Weight']=row['Weight']*-1
        print(row['Weight'])
        df1.at[index,'Weight']=row['Weight']
print(df1.Weight)
df1.to_csv('C:/Users/Iswarya/Documents/Bal_FlowDiffTotalAbs.csv')