class Solution:

    def findErrorNums(self, nums) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        N = len(nums)
        count = [0]* (N+1)
        for x in nums:
            count[x] += 1        
        for x in range(1,N+1):
            if count[x] == 2:
                dup = x
            if count[x] == 0:
                missing = x
                
        return [dup,missing]
