import pandas as pd 
import networkx as nx
g=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/ZJ_MstLenCol-2.csv')
for index,row in df1.iterrows():
    g.add_edge(row['Source'], row['Target'])
d=nx.single_source_shortest_path_length(g,114)
#print(d)
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys
lvl={}
for i in range(18):
    l=[]
    for key in getKeysByValue(d,i):
        l.append(key)
    lvl[i]=l
print(lvl)
