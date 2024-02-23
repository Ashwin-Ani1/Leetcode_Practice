class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        hashMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n] = i
        return 
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        # hashMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashMap:
        #         return [hashMap[diff],i]
        #     hashMap[n] = i
        # return 
        
        
        # #My solution
        # n=0 
        # while n != len(nums): #loop through the list
        #     i = n + 1 #i represents the next value of n 
        #     while i != (len(nums)): 
        #         if nums[n] + nums[i] == target:
        #             return [n,i] #Nested loop so its o(n^2) complexity
        #         i += 1 
        #     n+=1                                
        