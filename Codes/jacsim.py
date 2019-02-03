import pandas as pd 
import networkx as nx
import csv
from collections import defaultdict

def dfs(adj_list, visited, vertex, result, key):
    visited.add(vertex)
    result[key].append(vertex)
    for neighbor in adj_list[vertex]:
        if neighbor not in visited:
            dfs(adj_list, visited, neighbor, result, key)



def jaccard_similarity(list1, list2):
    c=0
    d=0
    for i,j in enumerate(list1):
        if list1[i]==1 and list2[i]==1:
            c=c+1
            d=d+1
        if  list1[i]==0 and list2[i]==1:
            d=d+1
        if  list1[i]==1 and list2[i]==0:
            d=d+1
    return (c/d)
            
df1=pd.read_csv("C:/Users/Iswarya/Documents/bla_fd_vec.csv")
g=nx.Graph()
for index,row in df1.iterrows():
    g.add_edge(row['Source'], row['Target'])
ed=g.edges()
dct={}

for i in range(1,31):
    for j in range(1,31):
        l=df1['L'+str(i)]
        n=df1['L'+str(j)]
        if i<j:
            dct[(i,j)]=  jaccard_similarity(l,n)
            #print(i,j,dct[(i,j)])

edges=[]
dct_thres={ k:v for k, v in dct.items() if v>0.4 and v<1 }
for item in dct_thres.keys():
    if (item[0],item[1]) in ed or (item[1],item[0]) in ed:
        edges.append(item)
##dct_thres={ k:v for k, v in dct.items() if v>0.8 and v<1}
##edges = dct_thres.keys()

adj_list = defaultdict(list)
for x, y in edges:
    adj_list[x].append(y)
    adj_list[y].append(x)

result = defaultdict(list)
visited = set()
for vertex in adj_list:
    if vertex not in visited:
        dfs(adj_list, visited, vertex, result, vertex)
#print('Ans')
#print(result.values())
ans=result.values()
li=[]
s=0
import numpy as np
for lt in ans:
   l=len(lt)
   maxi=0
   #u=(lt[0],lt[1]) #ALTERNATE
##   for i in range(0,l-1):
##       for j in range(1,l):
##           if (lt[i],lt[j]) in edges and maxi<dct_thres[(lt[i],lt[j])]:
##               maxi=dct_thres[(lt[i],lt[j])]
##               u=(lt[i],lt[j])
   for i in lt:
       for j in lt:
           if (i,j) in edges and maxi<dct_thres[(i,j)]:
               maxi=dct_thres[(i,j)]
               u=(i,j)

   #print(u)
   li.append(u)

               
print(li)

def entropy(dist):
    """
    Returns the entropy of `dist` in bits (base-2).
    """
    dist = np.asarray(dist)
    ent = np.nansum( dist *  np.log2( 1/dist ) )
    return ent
    #dist=[]

for lt in ans:
    dist=[]
    print(lt)
    for i in lt:
        for j in lt:
            if (i,j) in edges:
                #print((i,j))
                dist.append(dct_thres[(i,j)])
    #print(entropy(dist))
    s+=entropy(dist)
print(s)

df2=pd.read_csv("C:/Users/Iswarya/Documents/fd130.csv")                

lvec=[]
for item in li:
    #print(item[0])
    #print(item[1])
    vec=[]
    for index,row in df2.iterrows():
        if row['Source']==item[0] and row['Target']==item[1] or row['Source']==item[1] and row['Target']==item[0]:
            for i in range(1,31):
                vec.append(row['D'+str(i)])
                
    #print(vec)
    lvec.append(vec)
##
##print(lvec[0])
##print(lvec[1])
p=len(li)

from scipy import spatial

cos_sim=[]

for i in range(0,p-1):
    for j in range(i+1,p):
        result = 1 - spatial.distance.cosine(lvec[i], lvec[j])
        #print(result)
        cos_sim.append(result)
            
print(cos_sim)
print(sum(cos_sim)/len(cos_sim))

