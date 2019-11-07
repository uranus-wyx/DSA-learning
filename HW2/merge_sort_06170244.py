#!/usr/bin/env python
# coding: utf-8

# In[4]:


###### merge_sort_06170244.py

class Solution(object):
    
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        if len(nums)<=1:
            return nums   #如果nums裡面的元素不小於1，回傳mylist[]。

        i,j=0,0
        res =[]  #設兩個變數i,j，再設一個空的res集合，等等要將比較出來的數值放進去

        if len(nums)>1:
            mid = int(len(nums)//2)  #從nums裡找出中間的元素
            left = nums[:mid]  #index(0)～index(mid-1)（因為python是從0開始，所以取出來的值只包含開頭，不包含結束）
            right = nums[mid:]  #index(mid)～index(end)，省略終點，會直接算到最後一個index
            left = self.merge_sort(left)  
            right = self.merge_sort(right) #呼叫自己，這兩行是為了將nums裡的元素一個個分開，因為是位於Solution這個class裡，所以要self.merge_sort()

            while i<len(left) and j<len(right): #使用while條件迴圈，當i(left)＆j(right)同時小於組裡的長度時，會進行下一步，反之，若有條件不符，則不會繼續進行
                if left[i] < right [j]:
                    res.append(left[i])  
                    i+=1
                elif left[i] > right[j]:
                    res.append(right[j])
                    j+=1                       #用append的方式將左邊和右邊相對較小的left[i] or right[j]放入新的res[]裡，哪方的值被丟出來，那一方的變數（i,j）+=1，為了往下個值比較。

            res+=left[i:]+right[j:] #如果有一邊已經跑完了迴圈，這一步是以追加方式，將剩餘的元素加進res裡

        return res


# In[5]:


nums = [3,1,5,8,2,7,9,4,6]
output = Solution().merge_sort(nums)
output


# In[ ]:




