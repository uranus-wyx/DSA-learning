#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices   #幾個頂點
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 

        self.graph.append([u,v,w])
        
    def Dijkstra(self, s): 

        nopass = [i for i in range (0,len(self.graph))]  #[0,1,2,3,4,5,6,7,8]
        visited = []  
        
        if s in nopass:
            visited.append(s)  
            nopass.remove(s)
            
        dis = [float("inf")]*self.V  
        
        for n in range (0,len(self.graph[s])):
            if self.graph[s][n] != 0:
                dis[n] = self.graph[s][n]  
                
        dis[s]=0 
                             
        while len(nopass):     
            index = nopass[0]  
            def min_path(dis):        
                mi = float("inf")     
                for k in nopass:      
                    if dis[k] < mi:   
                        mi = dis[k]  
                        min_index = k 
                return min_index
            
            m = min_path(dis)         
            
            for k in nopass:          
                if (dis[m] + self.graph[m][k] < dis[k]) and self.graph[m][k]!=0:
                    dis[k] = dis[m] + self.graph[m][k] 
                    
            if m in nopass:
                nopass.remove(m)
            visited.append(m)
            
            dictionary = {}
            for d in range(0,self.V):
                dictionary[str(d)]= dis[d]
                
        return dictionary

    def Kruskal(self):
        """
        :rtype: dict
        """
        self.graph =  sorted(self.graph,key=lambda item: item[2])  
        
        i = 0
        parent = [-1]*self.V     
        visited = []             
        dictionary={} 
                
        while i < self.V:         
            
            for j in range (0,len(self.graph[i])): 

                if j==0 and self.graph[i][0] not in visited:     
                        parent[self.graph[i][j]]=self.graph[i][j]
                        visited.append(self.graph[i][j])
                    
                elif j==1 and parent[self.graph[i][0]] != parent[self.graph[i][1]]:

                    if self.graph[i][j] not in visited:
                        parent[self.graph[i][j]]=parent[self.graph[i][0]]
                        visited.append(self.graph[i][j])

                    else:
                        m=0
                        root = parent[self.graph[i][j]]
                        parent[self.graph[i][j]] = parent[self.graph[i][0]]
                        while m < len(parent):
                            if parent[m] == root:
                                parent[m] = parent[self.graph[i][0]] 
                            m+=1
 
                    a = str(self.graph[i][0])
                    b = str(self.graph[i][1])
                    c = str(a+"-"+b)
                    dictionary[str(c)] = self.graph[i][2]
            i+=1
        return dictionary

