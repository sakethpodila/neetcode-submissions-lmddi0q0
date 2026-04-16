class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = collections.defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        res = []
        for key, value in hm.items():
            if value > len(nums)//3:
                res.append(key)
        
        return res