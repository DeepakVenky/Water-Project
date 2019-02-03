import pandas as pd 
import networkx as nx
import operator
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
        
g=nx.Graph()
G=nx.Graph()
df1=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-2.csv')
for index,row in df1.iterrows():
    if row['Weight']!=0:
        g.add_edge(row['Source'], row['Target'])
d=to_dict_of_lists(g)
e=getRoots(d)
print(e)
df=pd.read_csv('F:/WaterCsv/ZJ_PressureDiffAll.csv')
#print(df['Diff1'])
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])

visited={}
nodewt={}
path={}  ### Stores all the nodes' path from source when the leak is at the node.

                
for i in range(1,114):
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
#print(newpath)
for k,item in newpath.items():
    #print(item)
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
#print(df2)
G2=nx.Graph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=1+1/row['Weight'])
pc=nx.betweenness_centrality(G2,weight='weight')
#print(pc)
sorted_cen = sorted(pc.items(), key=operator.itemgetter(1),reverse=True)

def get_senp(e):
    vis={}
    for (i,lt) in enumerate(e.values()):
        vis[i]=0
    lev=[]
    fornext=[]
    for k in sorted_cen:
        for (i,lt) in enumerate(e.values()):
            #print(k)
            #print(lt)
            if k[0] in lt and vis[i]==0:# and len(lt)>5:
##                for item in prev:
##                    #print(item)
##                 if nx.shortest_path_length(G,source=k[0][0],target=item[0][0])<1:
##                        #print(nx.shortest_path_length(G,source=k[0][0],target=item[0][0]))
##                #HOPS CHECK
##                        f=1
##                        break
##                if f==0:
##                    lev.append(k)
                lev.append(k)
                vis[i]=1
##            #elif f0==0 or f1==0:
            else:
                fornext.append(k)
    return lev
prsen=get_senp(e)
print(prsen)

#######REDUCING THE NUMBER OF SENSORS
####newG=nx.Graph()
####for (i,lt) in enumerate(e.values()):
####    newG.add_node(i+115)
####
####for(i,lt) in enumerate(e.values()):
####    for (j,lt2) in enumerate(e.values()):
####        for node in lt:
####            for ng in G2.neighbors(node):
####                if ng not in lt and ng in lt2:
####                    newG.add_edge(i+115,j+115)
####
####print(newG.edges())
##
##from networkx.algorithms import bipartite
##col=bipartite.color(newG)
##print(col)
##
sentr={}
for i in prsen:
    sentr[i]=True
for i in prsen:
    for j in prsen:
        if i!=j:
            dst=nx.shortest_path_length(G2,i[0],j[0])
            for lt in e.values():
                if i[0] in lt:
                    szi=len(lt)
                if j[0] in lt:
                    szj=len(lt)
            sz=min(szi,szj)
            if dst<sz/3:
                if i[1]<j[1]:
                    sentr[i]=False
                else:
                    sentr[j]=False
print(sentr)
                
