class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for n in s:
            if n == "(" or n == "{" or n == "[":
                arr.append(n)
            elif n == ")":
                if not arr or arr[-1] != "(":
                    return False
                arr.pop()
            elif n == "}":
                if not arr or arr[-1] != "{":
                    return False
                arr.pop()
            elif n == "]":
                if not arr or arr[-1] != "[":
                    return False
                arr.pop()    
        if not arr:
            return True    
        return False