import pandas as pd 
import networkx as nx
import operator
import xlrd
import csv

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

def get_sen(e,prev,G):
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
            if k[0] in lt and vis[i]==0 and len(lt)>2:
                lev.append(k)
                vis[i]=1
##            #elif f0==0 or f1==0:
            else:
                fornext.append(k)
    return lev

def getpath(v,nw,vis,G):
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
                    p.extend(getpath(nv,nw,vis,G))
                    return p
            return p

visited={}
G0=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/edges.csv')
df=pd.read_csv('F:/WaterCsv/ZJ-Flow/FlowDiffAll.csv')
for index,row in df1.iterrows():
    G0.add_edge(row['Source'], row['Target'])
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



dflev1=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-3.csv')
dflev2=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-2.csv')
dflev3=pd.read_csv('F:/WaterCsv/ZJ_MstLenCol-1.csv')


lev1=[]
lev2=[]
lev3=[]
e1=[]
e2=[]
e3=[]
for levels in range(1,4):
    if levels==1:
        e1=get_connected(dflev1)
        lev1=get_sen(e1,lev1,G0)
        #print("Length of lev 1",len(e))
    if levels==2:
        e2=get_connected(dflev2)
        lev2=get_sen(e2,lev1,G0)
        #print("Length of lev 2",len(e))
    if levels==3:
        e3=get_connected(dflev3)
        lev3=get_sen(e3,lev2,G0)
        #print("Length of lev 3",len(e))
        
#print("Level 1",lev1)
#print("Level 2",lev2)
#print("Level 3",lev3)

        
g=nx.Graph()
G=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/ZJ_MstLenCol-1.csv')
for index,row in df1.iterrows():
    if row['Weight']!=0:
        g.add_edge(row['Source'], row['Target'])
d=to_dict_of_lists(g)
e=getRoots(d)
#print(e)
df=pd.read_csv('C:/Users/Iswarya/Documents/ZJ_PressureDiffAll.csv')
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])

visited={}
nodewt={}
path={}

                
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
    path[i]=getpath(i,nodewt,vis,G)

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
G3=nx.Graph()
for index,row in df2.iterrows():
    G3.add_edge(row['Source'], row['Target'],weight=1+1/row['Weight'])
pc=nx.betweenness_centrality(G3,weight='weight')
#print(pc)
sorted_cenp = sorted(pc.items(), key=operator.itemgetter(1),reverse=True)

#print(get_senp(e))
import numpy as np
dfup=pd.read_csv('C:/Users/Iswarya/Documents/ZJ-PressureDiffL8.csv')
dfuf=pd.read_csv('C:/Users/Iswarya/Documents/ZJ-FlowDiffL8.csv')
uf=[]
ulf=dfuf['Abs0.25']
uf=[ulf[5],ulf[45],ulf[49],ulf[58],ulf[76],ulf[92],ulf[93],ulf[99],ulf[80],ulf[88]]
print(e2)
print(len(e2))

idx = np.argsort(uf)[-4:]
##l=e2
##if 0 in idx:
##    l.pop(7)
##    l.pop(4)
##    l.pop(3)
if ulf[88]>ulf[80]:
    e2.pop(7)
    e2.pop(4)
    e2.pop(3)
    e2.pop(2)
    e2.pop(1)
    e2.pop(0)

elif ulf[45]>ulf[5]:
    e2.pop(7)
    e2.pop(6)
    e2.pop(5)
    e2.pop(4)
    e2.pop(1)
    e2.pop(0)
elif ulf[76]>ulf[5]:
    e2.pop(7)
    e2.pop(6)
    e2.pop(5)
    e2.pop(3)
    e2.pop(2)
    e2.pop(1)
    e2.pop(0)
elif ulf[92]>ulf[5]:
    e2.pop(5)
    e2.pop(1)
    e2.pop(0)

elif ulf[99]>ulf[5]:
    e2.pop(7)
    e2.pop(3)
    e2.pop(2)
    e2.pop(1)
    e2.pop(0)
elif ulf[80]>ulf[88]:
    #l=e2
    if 7 in idx:
        e2.pop(0)
        e2.pop(1)
        e2.pop(2)
        e2.pop(3)
        e2.pop(4)
        e2.pop(5)
        e2.pop(7)
        
    else:
        e2.pop(6)
        e2.pop(5)
        if ulf[92]<ulf[5]:
            e2.pop(5)
        if ulf[58]>ulf[76]:
            e2.pop(4)
            e2.pop(2)
            e2.pop(0)
        else:
            e2.pop(3)
            e2.pop(1)
    
    
#e2=[list(x) for x in set(tuple(x) for x in e2).intersection(set(tuple(x) for x in l))]      
print(e2)
print(len(e2))
finp={}
for item in e2:
    for p,j in sorted_cenp:
        if p in item:
            finp[p]=j
sorted_finp = sorted(finp.items(), key=operator.itemgetter(1),reverse=True)

print(finp)
for item in e3:
    if list(finp.keys())[0] in item:
        print(item)
        break    
    

    

