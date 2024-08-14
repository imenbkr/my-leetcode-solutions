class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #stack of characters
        stack=[]
        
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='(' or s[i]=='[':
                stack.append(s[i])
            else : 
                if not stack:
                    return False

                if (ord(s[i])-2) == ord(stack[-1]) or (ord(s[i])-1) == ord(stack[-1]):
                    stack.pop()
                else:
                    return False
                
        return not stack 