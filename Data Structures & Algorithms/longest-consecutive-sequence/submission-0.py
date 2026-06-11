class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for i in nums:
            if i-1 not in nums:
                cnt=1
                cur=i
                while cur+1 in nums:
                    cur+=1
                    cnt+=1
                ans=max(ans,cnt)
        return ans





        