#!/usr/bin/env python
# coding: utf-8

# In[1]:


###### heap_sort_06170244.py
class Solution(object):
        
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
            #上面三行if就是爸爸和兒子們的數值比較，三者最大的index位置將成為爸爸的去處，前提是孩子們都不得大於數列的長度，因為有的孩子們並沒有開枝散葉
            # 但當爸爸發現手裡的數值並不是原本自己的，交換數值，但是這樣不夠，因為不知道下面的孩子們會不會有可以把自己打趴的，所以再次呼叫函數，往下比較


# In[2]:


nums = [3,2,4,1,5]
output = Solution().heap_sort(nums)
output


# In[ ]:




