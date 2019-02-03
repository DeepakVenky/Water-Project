# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:13:57 2018

@author: Iswarya
"""

# Boruvka's algorithm to find Minimum Spanning
# Tree of a given connected, undirected and weighted graph
import numpy as np
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
        self.mst=[]
        self.id=[]
       
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u-1,v-1,w])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        #print(i)
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's algorithm
    def boruvkaMST(self):
        j=0
# =============================================================================
#         for i in g.id:
#             j=j+1
#             self.colnode.update({i:j})
# =============================================================================
        parent = []; rank = []; 
 
        # An array to store index of the cheapest edge of
        # subset. It store [u,v,w] for each component
        cheapest =[]
        #cheapest=[]
        # Initially there are V different trees.
        # Finally there will be one tree that will be MST
        numTrees = self.V
        MSTweight = 0
 
        # Create V subsets with single elements
        for node in range(self.V):
            #j=0
            parent.append(node)
            #j=j+1
            rank.append(0)
            #cheapest.update({node:-1})
            cheapest=[-1]* self.V
        #print(cheapest)
        #print(parent)
        # Keep combining components (or sets) until all
        # compnentes are not combined into single MST
        newwt=1
        col=0
        while numTrees > 1:
            
            print("****************")
            
            # Traverse through all edges and update
               # cheapest of every component
            for i in range(len(self.graph)):
 
                # Find components (or sets) of two corners
                # of current edge
                u,v,w =  self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent ,v)
                #print(i)
                #print("sets %d %d", set1,set2)
                # If two corners of current edge belong to
                # same set, ignore current edge. Else check if 
                # current edge is closer to previous
                # cheapest edges of set1 and set2 .get(set1)
                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w :
                        cheapest[set1] = [u,v,w] 
 
                    if cheapest[set2] == -1 or cheapest[set2][2] > w :
                        cheapest[set2] = [u,v,w]

            # Consider the above picked cheapest edges and add them
            # to MST
            for node in range(self.V):
 
                #Check if cheapest for current set exists
                if cheapest[node] != -1:
                    u,v,w = cheapest[node]
                    #print(u)
                    set1 = self.find(parent, u)
                    set2 = self.find(parent ,v)
 
                    if set1 != set2 :
                        MSTweight += w
                        #print('*')
                        if newwt<2:
                            self.union(parent, rank, set1, set2)

                        #else:
                        #    self.union(parent, rank, get_first_key(set1), get_first_key(set2))
                            self.mst.append([u+1,v+1,newwt])
                        #print(rank)
                        print ("Edge %d-%d with weight %d included in MST=%d" % (u,v,w,col))
                        numTrees = numTrees - 1
             
            #reset cheapest array
            for node in range(self.V):
                cheapest =[-1] * self.V
            newwt=newwt+1
        
        print ("Weight of MST is %d %d" % (MSTweight,newwt))

import pandas as pd 

df1=pd.read_csv('F:/WaterCsv/ZJ_FlNoLeak.csv')
#mydf=pd.read_csv('C:/Users/Iswarya/Documents/Bal_latlon.csv')
g = Graph(114)
#print(mydf['Id'])
#g.addallid(mydf['Id'])
#print(g.id)
k=0
for index,row in df1.iterrows():
    k=k+1
    g.addEdge(row['Source'].astype(int), row['Target'].astype(int), row['Weight'].astype(int))
    #print(row['Source'].astype(int),row['Target'].astype(int),row['Weight'].astype(float))
    #if k == 164:
     #   break
#print(g.graph)
g.boruvkaMST()
print(g.mst)
df2=pd.DataFrame(g.mst)
df2.columns=['Source','Target','Weight']
df = pd.merge(df1, df2, on=['Source','Target'], how='left', indicator='Exist')
#df.drop('Weight', inplace=True, axis=1)
df['Exist'] = np.where(df.Exist == 'both', True, False)
#print (df)
df['Weight_y'].fillna(0, inplace=True)

df3=pd.DataFrame( {
      'Source': df['Source'],
      'Target': df['Target'],
      'Weight': df['Weight_y']
     })
print(df3)
df3.to_csv('C:/Users/Iswarya/Documents/ZJ_MstFloNoLkCol-1.csv')
# =============================================================================
# m=[]
# df1=DataFrame(g.mst)
# for index,row in df.iterrows():
#     if row in df1:
#         m.append(1)
#     else:
#         m.append(0)
# 
# =============================================================================

#df1=df1.transpose()
#df1.columns=['Source','Target','Weight']
#print(df1)
# =============================================================================
# m=[]
# for index,row in df.iterrows():
#     if row['Exist']==True:
#         m.append(5)
#     else:
#         m.append(1)
# print (m)
# df1=pd.DataFrame( {#'Id': l1,
#      'Source': df['Source'],
#      'Target': df['Target'],
#      'Weight': m
#     })
# df1.to_csv('C:/Users/Iswarya/Documents/mst_length.csv')
# =============================================================================
