#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self,val):
        
        self.val = val
        self.next = None
        
class MyHashSet:
    
    def __init__(self, capacity=5):
    
        self.capacity = capacity
        self.data = [None] * capacity
        
    def convert(self,key):
        
        code = MD5.new()
        code.update(key.encode("utf-8"))
        code.hexdigest()
        int(code.hexdigest(),16)
        return int(code.hexdigest(),16)
        
    def add(self, key):
        
        count = self.convert(key)
        index = count % self.capacity
        
        if self.data[index] is None:
            self.data[index] = ListNode(count)
            
        else:
            
            head = self.data[index]
            
            while head.next is not None:
                head = head.next
                
            head.next = ListNode(count)


    def remove(self, key):
           
        count = self.convert(key)
        
        if self.contains(key) == True:
            
            index = count % self.capacity
            
            if self.data[index].val == count:
                self.data[index]= self.data[index].next
            
            else:
                head = self.data[index]
                while head.next != count: 
                    head = head.next
                head.next = head.next.next
            
        if self.contains(key):
            self.remove(key)
            
        return
            
                
    def contains(self, key):
       
        count = self.convert(key)
        index = count % self.capacity
        
        if self.data[index] is None:
            return False
        else:
            head = self.data[index]
            while head is not None and head.val != count:
                head = head.next
            if head is not None:
                return True
            else:
                return False    


# In[2]:


hashSet = MyHashSet(10)
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
hashSet.contains("pig")


# In[3]:


hashSet.add("dog")
hashSet.remove("dog")
hashSet.contains("dog")


# Reference
# * [HashTable 的 Python 实现](https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/)
