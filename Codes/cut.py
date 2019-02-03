import pandas as pd 
import networkx as nx
G=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/edges.csv')
for index,row in df1.iterrows():
    if row['Source']!=114 and row['Target']!=114:
        G.add_edge(row['Source'], row['Target'])
    
print(nx.minimum_edge_cut(G,110,16))
