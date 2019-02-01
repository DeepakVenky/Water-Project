import pandas as pd 
import networkx as nx
import operator
import xlrd
import csv
visited={}
G=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/edges.csv')
df=pd.read_csv('F:/WaterCsv/ZJ-Flow/FlowDiffAll.csv')
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])
edgewt=[]
k=0
for i,row in df.iterrows():
    wt=0
    for j in range(1,114):
        if row['Diff'+str(j)]>0:
            wt+=row['Diff'+str(j)]
        else:
            wt+=row['Diff'+str(j)]*-1            
    edgewt.append(wt)
    k=k+1
    
df2=pd.DataFrame()
df2['Source']=df1['Source']
df2['Target']=df1['Target']
df2['Weight']=edgewt
#print(df2)

G2=nx.Graph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=1+1/row['Weight'])

mydict=nx.edge_betweenness_centrality(G2,weight='weight')
#print(mydict)
sorted_cen = sorted(mydict.items(), key=operator.itemgetter(1),reverse=True)
#print(sorted_cen)

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
def get_connected(dflev):
    g=nx.Graph()
    for index,row in dflev.iterrows():
        if row['Weight']!=0:
            g.add_edge(row['Source'], row['Target'])
    k=0
    d=to_dict_of_lists(g)
    cc=list(getRoots(d).values())
    #print(cc)
    return cc

dflev1=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-3.csv')
dflev2=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-2.csv')
dflev3=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-1.csv')

def get_sen(e,prev):
    vis={}
    for (i,lt) in enumerate(e):
        vis[i]=0
    lev=[]
    fornext=[]
    for k in sorted_cen:
        for (i,lt) in enumerate(e):
            f=0
            if k[0][0] in lt and k[0][1] in lt and vis[i]==0 and k not in prev:
                for item in prev:
                    #print(item)
                    if nx.shortest_path_length(G,source=k[0][0],target=item[0][0])<1:
                        #print(nx.shortest_path_length(G,source=k[0][0],target=item[0][0]))
                #HOPS CHECK
                        f=1
                        break
                if f==0:
                    lev.append(k)
                    vis[i]=1
##            #elif f0==0 or f1==0:
##            else:
##                fornext.append(k)
    return lev

lev1=[]
lev2=[]
lev3=[]
for levels in range(1,4):
    if levels==1:
        e=get_connected(dflev1)
        lev1=get_sen(e,lev1)
        print("Length of lev 1",len(e))
    if levels==2:
        e=get_connected(dflev2)
        lev2=get_sen(e,lev1)
        print("Length of lev 2",len(e))
    if levels==3:
        e=get_connected(dflev3)
        lev3=get_sen(e,lev2)
        print("Length of lev 3",len(e))
        
print("Level 1",lev1)
print("Level 2",lev2)
print("Level 3",lev3)
