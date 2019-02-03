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
df1=pd.read_csv('C:/Users/Iswarya/Documents/ZJ_MstLenCol-3.csv')
df=pd.read_csv('C:/Users/Iswarya/Documents/FlowDiffAll.csv')
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
import numpy as np

fin={}
acco={}
#6,49,54,63,86,108,109,115
for key,lt in e.items():
    newd={6:0,49:0,54:0,63:0,86:0,108:0,109:0,115:0,94:0,103:0}
    acci={6:0,49:0,54:0,63:0,86:0,108:0,109:0,115:0,94:0,103:0}
    for item in lt:
        kn=[]
        if item!=114:
            l=df['Diff'+str(item)]
##            newd[6]+=abs(l[5])
##            kn.append(abs(l[5]))
##            newd[49]+=abs(l[45])
##            kn.append(abs(l[45]))
##            newd[54]+=abs(l[49])
##            kn.append(abs(l[49]))
##            newd[63]+=abs(l[58])
##            kn.append(abs(l[58]))
##            newd[86]+=abs(l[76])
##            kn.append(abs(l[76]))
##            newd[108]+=abs(l[92])
##            kn.append(abs(l[92]))
##            newd[109]+=abs(l[93])
##            kn.append(abs(l[93]))
##            newd[115]+=abs(l[99])
##            kn.append(abs(l[99]))
            newd[94]+=abs(l[80])
            kn.append(abs(l[80]))
            newd[103]+=abs(l[88])
            kn.append(abs(l[88]))
            idx = np.argsort(kn)[-1:]
            #print(idx)
            if 0 in idx:
                acci[94]+=1
            if 1 in idx:
                acci[103]+=1
##            if 0 in idx:
##                acci[6]+=1
##            if 1 in idx:
##                acci[49]+=1
##            if 2 in idx:
##                acci[54]+=1
##            if 3 in idx:
##                acci[63]+=1
##            if 4 in idx:
##                acci[86]+=1
##            if 5 in idx:
##                acci[108]+=1
##            if 6 in idx:
##                acci[109]+=1
##            if 7 in idx:
##                acci[115]+=1
    acci = {k: v*100/ len(lt)  for k, v in acci.items()}#
    acco[key]=acci
    fin[key]=newd
print(fin)
print(acco)
