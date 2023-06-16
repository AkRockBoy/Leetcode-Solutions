class Solution:
    def isValid(self, s: str) -> bool:
        dt={'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in dt:
                stack.append(dt[i])
            elif len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
                
        