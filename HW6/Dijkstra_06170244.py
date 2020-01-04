#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices  
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """       
        self.graph.append([u,v,w])

    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        #nopass = [False]*self.V
        nopass = [i for i in range (0,len(g.graph))]  #[0,1,2,3,4,5,6,7,8]
        visited = []  #將已經確定頂點s(0)到i(1~8)的距離放進
        
        if s in nopass:
            visited.append(s)   #[0]頂點放入
            nopass.remove(s)    #[1,2,3,4,5,6,7,8] 頂點移出
            
        dis = [float("inf")]*self.V  #頂點s(0)到i(1~8)的距離，確定的取代dis中的無限值
                                     #[inf,inf,inf,inf,inf,inf,inf,inf,inf]
        
        for n in range (0,len(g.graph[s])):
            if g.graph[s][n] != 0:
                dis[n] = g.graph[s][n]  #因為測資的值中，一開始會知道頂點到某點的距離，那麼dis裡的值就會被取代
                                        #[0,4,inf,inf,inf,inf,inf,8,inf]
                
        dis[s]=0 #頂點s到頂點s的距離皆為0
                            
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
                if (dis[m] + g.graph[m][k] < dis[k]) and g.graph[m][k]!=0:
                        dis[k] = dis[m] + g.graph[m][k] 
                    
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

