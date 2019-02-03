import pandas as pd
import numpy as np
import xlrd 

#file1 = r'D:/Research Project/NETWORK/ZJ/Pressure_NoLeak.csv'
#file2 = r'D:/Research Project/NETWORK/ZJ/Pressure_L12-100.csv'

df1 = pd.read_csv("F:/WaterCsv/ZJ_PrNoLeak.csv")
#print(df1['T1'])

df4=pd.DataFrame()
df4['ID']=df1.iloc[:-1,0]

for i in range(1,114):
    
    df2 = pd.read_csv("F:/WaterCsv/EPANET pressure values/node_"+str(i)+".csv")
    #print(df2['T1'])

    d1=df2.iloc[:,1]-df1.iloc[:,1]


    print(d1)


    np.savetxt("C:/Users/Iswarya/Documents/Pressure_Diff_dummy.csv", d1, delimiter=",", fmt='%s', header='Result')

    df3=pd.read_csv("C:/Users/Iswarya/Documents/Pressure_Diff_dummy.csv")
    #print(df3)

    df4['Diff'+str(i)]=df3.iloc[:-1,0]
    #df4['Rank']=df4['Diff'].rank(ascending=False)

print(df4)

df4.to_csv("C:/Users/Iswarya/Documents/ZJ_PressureDiffAll.csv")





