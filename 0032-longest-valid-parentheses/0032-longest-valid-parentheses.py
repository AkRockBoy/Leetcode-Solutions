class Solution:
    def longestValidParentheses(self, s: str) -> int:
       
        op , cl = 0 , 0
        mx = 0
        for i in s:
            if i =='(': 
                op += 1
            else: 
                cl += 1
            if op == cl: 
                mx = max(mx,cl*2)
            elif cl > op:
                op , cl = 0 , 0

        op , cl = 0 , 0
        for i in s[::-1]:
            if i == ')': 
                cl += 1
            else: 
                op += 1
            if op == cl: 
                mx = max(mx,cl*2)
            elif op > cl:
                op , cl = 0 , 0
        return mx


        '''
        stack = []
        index = [-1]
        mx = 0
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(s[i])
                index.append(i)
            else:
                index.pop()
                if not index:
                    index.append(i)
                else:
                    stack.pop()
                    mx = max(mx,i-index[-1])  
        return mx
        '''
        '''
        stack = [-1]
        mx = 0
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx,i-stack[-1])
        return mx
        '''

                


                    

        