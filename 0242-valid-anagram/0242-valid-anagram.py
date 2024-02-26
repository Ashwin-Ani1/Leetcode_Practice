class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(str(s)) == sorted(str(t))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #Solution 1
#         #time and space complexity o(N) or o(s+t) since we are looping through both strings
#         if len(s) != len(t):  #base case to check if they have the same # in total
#             return False
        
#         countS, countT = {},{} # Two hashmaps that can keep track of the count of var
        
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0) # can be done since same length
            
#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False
        
#         return True    
    
        #Solution 2 in an O(1) memory nothing really stored so you can sort and compare the only issue is time complexity can increase since sorting 
        #return sorted(str(s))  == sorted(str(t))
        
        #Solution 3
        #return Counter(s) == Counter(t) Fast one line solution data structure that is a hashmap that counts what was done exactly 
         
            