class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops='+-/*'
        stack=[]
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                y=stack.pop()
                x=stack.pop()
                if i=='+':
                    ans=x+y
                elif i=='-':
                    ans=x-y
                elif i=='*':
                    ans=x*y
                else:
                    ans=int(x/y)
                print(ans)
                stack.append(ans)
        return stack[-1]
            
            
        