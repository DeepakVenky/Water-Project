import pandas as pd
import numpy as np
import xlrd 

file1 = r'F:/WaterCsv/ZJ-Flow/FlowNoLeak.csv'
df1 = pd.read_csv(file1)
df4=pd.DataFrame()
df4['ID']=df1.iloc[:-1,0]

for i in range(1,114):

    df2 = pd.read_csv("F:/WaterCsv/ZJ-Flow/flow_"+str(i)+".csv")
    d1=df2.iloc[:-1,1]-df1.iloc[:-1,1]
    #print(d1)
    print(d1)
    
    np.savetxt("F:/WaterCsv/ZJ-Flow/Flow_Diff_dummy.csv", d1, delimiter=",", fmt='%s', header='Result')

    df3=pd.read_csv("F:/WaterCsv/ZJ-Flow/Flow_Diff_dummy.csv")
    #print(df3)

    df4['Diff'+str(i)]=df3.iloc[:,0]


print(df4)

df4.to_csv("F:/WaterCsv/ZJ-Flow/FlowDiffAll.csv")
