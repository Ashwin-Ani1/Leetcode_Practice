class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):  #base case to check if they have the same # in total
            return False
        
        countS, countT = {},{} # Two hashmaps that can keep track of the count of var
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0) # can be done since same length
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True        
            