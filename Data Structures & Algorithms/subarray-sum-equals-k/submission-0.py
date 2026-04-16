class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        summ = 0
        res = 0
        for num in nums:
            summ += num
            diff = summ - k
            res += hm.get(diff, 0) 
            if hm.get(summ, 0):
                hm[summ] += 1
            else: hm[summ] = 1
        
        return res
