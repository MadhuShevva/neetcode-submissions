import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            hrs=0
            for i in piles:
                hrs+=math.ceil(i/mid)
            if hrs<=h:
                right=mid
            else:
                left=mid+1
        return left

        