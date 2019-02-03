def to_dict_of_lists(G,nodelist=None):
    """Return adjacency representation of graph as a dictionary of lists.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    nodelist : list
       Use only nodes specified in nodelist

    Notes
    -----
    Completely ignores edge data for MultiGraph and MultiDiGraph.

    """
    if nodelist is None:
        nodelist=G

    d = {}
    for n in nodelist:
        d[n]=[nbr for nbr in G.neighbors(n) if nbr in nodelist]
    return d
def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {} 
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode,0)  
    for myI in aNeigh: 
        for myJ in aNeigh[myI]: 
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot) 
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot) 
            if myRoot_myI != myRoot_myJ: 
                myMin = myRoot_myI
                myMax = myRoot_myJ 
                if  myDepthMyI > myDepthMyJ: 
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1) 
    myToRet = {}
    for myI in aNeigh: 
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh: 
        myToRet[findRoot(myI,myRoot)[0]].append(myI) 
    return myToRet
import pandas as pd 
import networkx as nx
g=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/ZJ_MstLenCol-2.csv')
for index,row in df1.iterrows():
    if row['Weight']!=0:
        g.add_edge(row['Source'], row['Target'])
#d=to_dict_of_lists(g)
#e=getRoots(d)
#print(e)
#visited={}
G=nx.Graph()
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])
#b=list(nx.bfs_edges(G,114))
#print(b)
df2=pd.DataFrame()
df2['Source']=df1['Source']
df2['Target']=df1['Target']
df2['Weight']=0
#print(df2)
paths=[]
paths.append(nx.dijkstra_path(G,114,8))#1
paths.append(nx.dijkstra_path(G,114,93))#2
paths.append(nx.dijkstra_path(G,114,57))#3
paths.append(nx.dijkstra_path(G,114,40))#4
paths.append(nx.dijkstra_path(G,114,106))#5
paths.append(nx.dijkstra_path(G,114,36))#6
paths.append(nx.dijkstra_path(G,114,83))#7
paths.append(nx.dijkstra_path(G,114,15))#8
paths.append(nx.dijkstra_path(G,114,35))#9
paths.append(nx.dijkstra_path(G,114,108))#10
print(paths)
for path in paths:
    print(path)
    for i,j in enumerate(path[:-1]):
        df2.loc[(df2['Source'] == j) & (df2['Target'] == path[i+1]),'Weight']+=1
        #print(df2.loc[(df2['Source'] == j) & (df2['Target'] == path[i+1])])
df2.loc[df2['Target']==114,'Weight']=10
print(df2)
G2=nx.Graph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=row['Weight'])
print(nx.edge_betweenness_centrality(G))
print(nx.edge_betweenness_centrality(G2,weight='weight'))
