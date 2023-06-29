class Solution(object):
    def containsDuplicate(self, nums):
        #first sorted the array in order because I want to compare the values side by side
        nums.sort()
        #Had to do len(nums)-1 since I will get an error for a greater length
        #if at least one match there will be a return of true
        for i in range (len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True