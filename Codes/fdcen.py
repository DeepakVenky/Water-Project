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
print(df2)
G2=nx.DiGraph()
for index,row in df2.iterrows():
    G2.add_edge(row['Source'], row['Target'],weight=1+1/row['Weight'])
#print(nx.edge_betweenness_centrality(G))
mydict=nx.edge_betweenness_centrality(G2,weight='weight')
print(mydict)
with open('fd_centrality-ZJ-2.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key[0],key[1], value])

#print(nx.betweenness_centrality(G2,weight='weight'))







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
        if k[0] in l and k[1] in l and v >maxi :
            maxip = k
            maxi=v
    print(maxip)
    
