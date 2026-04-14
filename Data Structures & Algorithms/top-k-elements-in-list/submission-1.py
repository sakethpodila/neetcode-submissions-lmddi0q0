class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else: hm[num] = 1
        hm = sorted(hm.items(), key=lambda item:item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(hm[i][0])
        return res
        
            
            