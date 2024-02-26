class Solution:
    def isPalindrome(self, s):
        
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False                
            l+=1
            r-=1
        return True
        
            
        
        
        
        
        # #First initialize String    
        # Str = ""
        # #Create a new string with no spaces
        # for c in s:
        #     if c.isalnum():
        #         #make sure all alpha is lowercase
        #         Str += c.lower()
        # #compare the string and its reversed string
        # return Str == Str[::-1]
        # #Time O(n): loop through a string(n time)
        # #Space O(n): create a new string so memory being allocated

        