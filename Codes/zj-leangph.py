import pandas as pd 
import networkx as nx
import csv
df1=pd.read_csv('C:/Users/Iswarya/Documents/FlowDiffAll-2.csv')
df=pd.read_csv('C:/Users/Iswarya/Documents/zj_fd_vec.csv')
g=nx.DiGraph()
for index,row in df.iterrows():
    g.add_edge(row['Source'], row['Target'])
ed=g.edges()
for i in range(1,114):
    G=nx.DiGraph()
    print(i)
    for index,row in df1.iterrows():
        if row['Diff'+str(i)]>0:
            G.add_edge(row['Source'], row['Target'])
        elif row['Diff'+str(i)]!=0:
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
    #print(l)
print(df)
df.to_csv('C:/Users/Iswarya/Documents/zj_fd_vec.csv')            

    

    
