import pandas as pd 
import networkx as nx
import csv
df1=pd.read_csv('F:/WaterCsv/edges.csv')
df=pd.read_csv('F:/WaterCsv/ZJ-Flow/FlowDiffAll.csv')
g=nx.DiGraph()
ed=g.edges()
for index,row in df.iterrows():
    g.add_edge(row['Source'], row['Target'])
for i in range(1,114):
    G=nx.DiGraph()
    print(i)
    for index,row in df1.iterrows():
        if row['D'+str(i)]>0:
            G.add_edge(row['Source'], row['Target'])
        elif row['D'+str(i)]!=0:
            G.add_edge(row['Target'], row['Source'])
    lean=G.edges()
    #print(lean)
    bfs=nx.shortest_path(G,114,i)
    #print(bfs)
    l=[]
    for p in ed:
        if p in lean:
            l.append(1)
        else:
            l.append(0)
    df['L'+str(i)]=l
    print(l)
#print(df)
df.to_csv('C:/Users/Iswarya/Documents/zj_fd_vec.csv')            

    

    
