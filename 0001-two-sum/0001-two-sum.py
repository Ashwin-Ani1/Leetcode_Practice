class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=0
        while n != len(nums):
            i = n + 1
            while i != (len(nums)):
                if nums[n] + nums[i] == target:
                    return [n,i]
                i += 1
            n+=1                
                