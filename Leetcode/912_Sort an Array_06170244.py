class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len (nums)   
        parent = (n//2)-1  

        while parent >=0:
            self.heapify(nums,parent,n)  
            parent-=1  

        end = len(nums)-1
        while (end > 0):  
            nums[end] , nums[0] = nums[0] , nums[end]  
            self.heapify(nums, 0, end) 
            end -= 1 

        return nums #回傳nums

    def heapify(self,nums, i, n):  
        daddy = i
        leftkid = 2*i+1
        rightkid = 2*i+2  
        if leftkid < n and nums[daddy] < nums[leftkid]:
            daddy = leftkid
        if rightkid < n and nums[daddy] < nums[rightkid]:
            daddy = rightkid
        if daddy != i:
            nums [i] ,nums[daddy] = nums[daddy] , nums[i]
            self.heapify(nums,daddy,n)
        
     # return sorted(nums)
        

