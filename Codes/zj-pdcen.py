import pandas as pd 
import networkx as nx
import operator
visited={}
G=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/edges.csv')
df=pd.read_csv('F:/WaterCsv/ZJ_PressureDiffAll.csv')
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])
nodewt={}
path={}
def getpath(v,nw,vis):
    if v==114:
        p=[]
        p.append(114)
        return p
    else:
        l=list(G.neighbors(v))
        vis[v]=True
        #print(vis)
        p=[]
        if 114 in l:
            p.append(114)
            return p
        else:
            #print(l)
            for item in l:
                if vis[item]==False:
                    temp={}
                    for key in nw:
                        if key in l and vis[key]==False:
                            temp[key]=nw[key]
                    #print(temp)
                    nv=max(temp.items(), key=operator.itemgetter(1))[0]
                    #print(nv)
                    p.append(nv)
                    #print(vis)
                    p.extend(getpath(nv,nw,vis))
                    return p
            return p
                
for i in range(56,57):
    wt=df['Diff'+str(i)]
    #k=0
    for v in G.nodes():
        if v==114:
            nodewt[v]=5
        else:
            nodewt[v]=wt[v-1]
            #k=k+1
    #print(nodewt)
    vis={}
    for j in range(1,114):
        vis[j]=False
    path[i]=getpath(i,nodewt,vis)

df2=pd.DataFrame()
df2['Source']=df1['Source']
df2['Target']=df1['Target']
df2['Weight']=1
#print(path)
newpath={}
for key,value in path.items():
    newpath[key]=[]
    newpath[key].append(key)
    newpath[key].extend(value)
print(newpath)
for k,item in newpath.items():
    print(item)
    for i,j in enumerate(item[:-1]):#for using i+1
        #print(i,j)
        #print(item[i+1])
        if i==0 or j==110:
            df2.loc[(df2['Source'] == j) & (df2['Target'] == item[i+1]),'Weight']+=1
            #print(df2.loc[(df2['Source'] == j) & (df2['Target'] == item[i+1])])
        else:
            df2.loc[(df2['Source'] == item[i+1]) & (df2['Target'] == j),'Weight']+=1
            #print(df2.loc[(df2['Source'] == item[i+1]) & (df2['Target'] == j)])
#df2.loc[df2['Target']==114,'Weight']=113
print(df2)
G2=nx.Graph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=1+1/row['Weight'])
#print(nx.edge_betweenness_centrality(G))
#print(nx.edge_betweenness_centrality(G2,weight='weight'))

mydict=nx.betweenness_centrality(G2,weight='weight')
print(mydict)







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
evals=list(e.values())

for l in evals:
    maxi = 0
    for k,v in mydict.items():    
        if k in l and v >maxi :
            maxip = k
            maxi=v
    print(maxip)
    

