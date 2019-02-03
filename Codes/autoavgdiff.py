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
k=0
for index,row in df1.iterrows():
    if row['Weight']!=0:
        g.add_edge(row['Source'], row['Target'])
        #print(row['Source'].astype(int),row['Target'].astype(int),row['Weight'].astype(int))
    #if k == 57:
     #   break
d=to_dict_of_lists(g)
e=getRoots(d)
print(e)
##import csv
##with open('C:/Users/Iswarya/Documents/Bla-capcluster1.csv', 'w') as csv_file:
##    writer = csv.writer(csv_file)
##    for key in e:
##        for val in e[key]:
##            writer.writerow([key, val])
##df2=pd.read_csv('C:/Users/Iswarya/Documents/Pressure_Diff100.csv')
##from statistics import mean
##e2={}
##for key in e:
##    l=[]
##    s=0
##    c=0
##    for item in e[key]:
##        #print(item)
##        c=c+1
##        if item!=114:
##            l.append(df2.loc[df2['Id'] == item, 'Weight'].item())
##            s+=df2.loc[df2['Id'] == item, 'Weight'].item()
##    #print(l)
##    e2[key]=s/c
##print(e2)
##print(sorted(nx.connected_components(g), key = len, reverse=True))
##
