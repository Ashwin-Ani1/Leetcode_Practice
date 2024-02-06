class Solution(object):
    def containsDuplicate(self, nums):
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
        
        
            
    
    
    
    
    
        """
        
        nums.sort()
        #Had to do len(nums)-1 since I will get an error for a greater length
        #if at least one match there will be a return of true
        for i in range (len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        #time O(nlogn) due to sorting and space O(1)    
        
        # More efficient code that is timeCO{O(n)} Space O(n)
                #first sorted the array in order because I want to compare the values side by side
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        """