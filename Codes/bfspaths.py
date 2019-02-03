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
df2=pd.read_csv('C:/Users/Iswarya/Documents/edges.csv')
for index,row in df1.iterrows():
    if row['Weight']!=0:
        g.add_edge(row['Source'], row['Target'])
d=to_dict_of_lists(g)
e=getRoots(d)
print(e)
visited={}
G=nx.Graph()
for index,row in df2.iterrows():
    G.add_edge(row['Source'], row['Target'])
b=list(nx.bfs_edges(G,114))
print(b)
c=[]
print(nx.betweenness_centrality(G))
for key in e:
    visited[key]=0
for item in b:
    for key in e:
        if visited[key]==0:
            if item[0] in e[key] or item[1] in e[key]:
                c.append(item)
                visited[key]=1
                print(key)
##for key in e:
##    visited[key]=0
##keys = list(e.keys())
##for item in b:
##    if visited[keys[0]]==0:
##        c.append(item)
##        if item[0] in e[keys[0]] or item[1] in e[keys[0]]:
##            visited[keys[0]]=1
##            print(key)
print(c)
            
