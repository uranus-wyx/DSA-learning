#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices  
        self.graph = []
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """       
        self.graph.append([u,v,w])

    def Kruskal(self):
        """
        :rtype: dict
        """
        g.graph =  sorted(g.graph,key=lambda item: item[2])

        i = 0
        parent = [-1]*self.V     
        visited = []
        dictionary={} 
                
        while i < self.V:

            for j in range (0,len(g.graph[i])):

                if j==0:
                    if g.graph[i][0] not in visited:
                        parent[g.graph[i][j]]=g.graph[i][j]
                        visited.append(g.graph[i][j])

                elif j==1 and parent[g.graph[i][0]] != parent[g.graph[i][1]]:

                    if g.graph[i][j] not in visited:
                        parent[g.graph[i][j]]=parent[g.graph[i][0]]
                        visited.append(g.graph[i][j])

                    else:
                        m=0
                        root = parent[g.graph[i][j]]
                        parent[g.graph[i][j]] = parent[g.graph[i][0]]
                        while m < len(parent):
                            if parent[m] == root:
                                parent[m] = parent[g.graph[i][0]] 
                            m+=1

                    a = str(g.graph[i][0])
                    b = str(g.graph[i][1])
                    c = str(a+"-"+b)
                    dictionary[str(c)] = g.graph[i][2]
            i+=1
        return dictionary

