class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        for i in s:
            if i.isalnum():
                try:
                    s+=i.lower()
                except:
                    pass
        
        s=s[n:]
        print(s)
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
                exit()
            i+=1
            j-=1
        return True
                


        