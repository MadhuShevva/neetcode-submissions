class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        flg=False
        for i in nums:
            if i in d:
                flg=True
                return True
            else:
                d[i]=1
        return flg
        
        
        