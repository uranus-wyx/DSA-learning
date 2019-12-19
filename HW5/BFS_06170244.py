#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict  
class Graph:

    def __init__(self): 
        
        self.graph = defaultdict(list) 
    
    def addEdge(self,u,v): 
        
        self.graph[u].append(v) 
            
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        color = []       
        queue = [s]     #queue為一個已有起點s的list
        
        
        while queue:
            top = queue.pop(0) #將queue裡index = 0的值pop出為top
            
            if top not in color:
                color.append(top) 
                queue.extend(set(self.graph[top]) - set(color))
                
        return color

    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        color = list()
        queue = [s]
        
        def dfs(s):
            
            if queue:
                top = queue.pop(-1)

                if top not in color:
                    color.append(top)
                    i = queue.extend(set(self.graph[top]) - set(color))
                    dfs(i)
        dfs(s)
        return color

