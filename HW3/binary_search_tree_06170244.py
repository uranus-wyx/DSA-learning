#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
    def Printtree(self):
        
        if self.left:
            self.left.Printtree()
            
        print(self.val),
        
        if self.right:
            self.right.Printtree()
            
class Solution(object):
    
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        data = TreeNode(val)
        
        if root.val:    #root.val 存在，往下走
            if val <= root.val:
                
                if root.left is None:
                    root.left = data
                    return root.left            # if leftkid is empty, fill it
                else:
                    return self.insert(root.left,val)   # if leftkid has a val, again the function
                
            elif val > root.val:
               
                if root.right is None:    # same as leftkid
                    root.right = data
                    return root.right
                else:
                    return self.insert(root.right,val)
                
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
        node = self.search(root,target)
        parent = root
        
        if root == None:
            return root
        if node:
            if target < root.val:
                root.left = self.delete(root.left,target)
            elif target > root.val:
                root.right = self.delete(root.right,target)

            else:

                if root.left is None and root.right is None:
                    
                    root = None

                elif root.left and (root.right is None):                    
                    root = root.left
                    self.delete(root,target)

                elif (root.left is None) and root.right:
                    root = root.right
                    self.delete(root,target)

                elif root.left and root.right:
                    
                    parent = root
                    successor = root.right

                    while successor.left:
                        parent = successor
                        successor = successor.left

                    root.val = successor.val

                    if root == successor:
                        parent.left = successor.right
                    else:
                        parent.right = successor.right
            return root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target < root.val:
            if root.left == None:
                return None 
            return self.search(root.left,target)
        
        elif target > root.val:
            if root.right == None:
                return None
            return self.search(root.right,target)
        
        else:
            return root
    
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        old = self.Tree_array(root)
        new = []
        for i in old:
            if i == target:
                i = new_val
                new.append(i)
            else:
                new.append(i)
        
        new_array = self.heap_sort(new)
        new_root = len(new_array)//2
        new_data = TreeNode(new_array[new_root])
        
        for j in range(len(new_array)):
            if j != new_root:
                self.insert(new_data, new_array[j])

        return new_data
        
        
        
    def Tree_array(self, root):
        
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return vals
    #引用univaltree的方法，將node放進vals[]裡
    
    def heap_sort(self,nums):
        n = len (nums)    # n 是 nums數列長度
        parent = (n//2)-1  #最後一個父節點

        while parent >=0:  #當父節點>=0時，繼續執行
            self.heapify(nums,parent,n)  #呼叫Solution中的heapify函數，將所有父節點>子節點
            parent-=1  #parent會減少，因為要從最下面的節點開始篩選，一一往上

        end = len(nums)-1  #設end是數列長度減1，因為python的數列是從0開始，所以結束的位置是len(nums)-1

        while (end > 0):  #當end大於0時，下一步
            nums[end] , nums[0] = nums[0] , nums[end]  #此時因為上方已經呼叫了heapify函數，所以index(0)會是最大的值，跟最後一個元素的值交換
            self.heapify(nums, 0, end) #此步驟是因為上一步的交換使得index(0)不是數列中最大的值，所以再次呼叫heapify函數
            end -= 1  #每一次的迴圈中會把最大的值往最後一個元素放，所以下一次跑迴圈時，不可包含最後面已經交換完成的元素，因為它們已排列好
                
        return nums #回傳nums

    def heapify(self,nums, i, n):  #這個函數是為了讓heapsort呼叫而設的

        daddy = i
        leftkid = 2*i+1
        rightkid = 2*i+2  #爸爸、左邊小孩、右邊小孩，爸爸>左邊小孩、右邊小孩

        if leftkid < n and nums[daddy] < nums[leftkid]:
            daddy = leftkid
        if rightkid < n and nums[daddy] < nums[rightkid]:
            daddy = rightkid
        if daddy != i:
            nums [i] ,nums[daddy] = nums[daddy] , nums[i]
            self.heapify(nums,daddy,n)
        #引用自己的heap_sort


# In[2]:


root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8) 
root.left = Node1
Node1.left = Node2
Node2.left = Node3
root.right = Node4
a = Solution()
a.insert(root,7)
a.insert(root,6)
a.insert(root,10)


# In[3]:


a.delete(root,3)
root.Printtree()


# In[4]:


root = a.modify(root,6,9)
root.Printtree()


# In[ ]:




