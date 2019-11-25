#!/usr/bin/env python
# coding: utf-8

# In[40]:


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
        
    def count(self):
    
        count = 0
        if root.left:
            count +=1

        if root.right:
            count +=1

        return count
    
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        node = self.search(root,target)
        i = root
        
        while node != None:
    
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
                
            self.insert(i,new_val)
            return i

# In[41]:


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

