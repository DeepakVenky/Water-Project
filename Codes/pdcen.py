import pandas as pd 
import networkx as nx
import operator
visited={}
G=nx.Graph()
df1=pd.read_csv('C:/Users/Iswarya/Documents/bla_edges.csv')
df=pd.read_csv('C:/Users/Iswarya/Documents/PressureDiffAll.csv')
for index,row in df1.iterrows():
    G.add_edge(row['Source'], row['Target'])
nodewt={}
path={}
def getpath(v,nw,vis):
    if v==0:
        p=[]
        p.append(0)
        return p
    else:
        l=list(G.neighbors(v))
        vis[v]=True
        #print(vis)
        p=[]
        if 0 in l:
            p.append(0)
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
                
for i in range(1,31):
    wt=df['Diff'+str(i)]
    #k=0
    for v in G.nodes():
        if v==0:
            nodewt[v]=5
        else:
            nodewt[v]=wt[v-1]
            #k=k+1
    #print(nodewt)
    vis={}
    for j in range(1,31):
        vis[j]=False
    path[i]=getpath(i,nodewt,vis)

df2=pd.DataFrame()
df2['Source']=df1['Source']
df2['Target']=df1['Target']
df2['WeightRec']=1
#print(path)
newpath={}
for key,value in path.items():
    newpath[key]=[]
    newpath[key].append(key)
    newpath[key].extend(value)
print(newpath)
for k,item in newpath.items():
    #print(item)
    for i,j in enumerate(item[:-1]):#for using i+1
        #print(i,j)
        #print(item[i+1])
        if i==0:
            df2.loc[(df2['Source'] == j) & (df2['Target'] == item[i+1]),'WeightRec']+=1
            #print(df2.loc[(df2['Source'] == j) & (df2['Target'] == item[i+1])])
        else:
            df2.loc[(df2['Source'] == item[i+1]) & (df2['Target'] == j),'WeightRec']+=1
            #print(df2.loc[(df2['Source'] == item[i+1]) & (df2['Target'] == j)])
print(df2)
G2=nx.Graph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=1+1/row['WeightRec'])
#print(nx.edge_betweenness_centrality(G))
print(nx.edge_betweenness_centrality(G2,weight='weight'))
print(nx.betweenness_centrality(G2,weight='weight'))
