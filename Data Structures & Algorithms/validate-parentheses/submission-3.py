class Solution:
    def isValid(self, s: str) -> bool:
        mp={')':'(','}':'{',']':'['}
        n=len(s)
        stack=[]

        for i in range(n):
            print(stack)
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if stack and stack[-1]==mp[s[i]] :
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
                    
        