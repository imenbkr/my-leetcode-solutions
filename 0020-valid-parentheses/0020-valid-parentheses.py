class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'(': ')', '{':'}', '[':']'}

        stack=[]

        for i in s:
            if i in brackets:
                stack.append(i)
            elif i in brackets.values():
                if stack and brackets[stack[-1]]== i :
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
