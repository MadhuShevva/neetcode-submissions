from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        d=sorted(Counter(nums).items(),key = lambda x:x[1],reverse=True)
        l=[]
        for i in range(k):
            l.append(d[i][0])
        return l



        