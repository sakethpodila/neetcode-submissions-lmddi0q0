class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = collections.defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        count = 0
        for num in nums:
            temp = 0
            while hm[-~num]:
                num += 1
                temp += 1

            count = max(count, temp)
        
        if len(nums) == 0:
            return count
        return count + 1
            
