class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr_map = [0] * len(nums)
        res = 0
        for num in nums:
            if num > 0 and num <= len(nums):
                arr_map[num - 1] = 1
        
        for i in range(len(arr_map)):
            if not arr_map[i]:
                print(i)
                return i + 1
        
        return len(nums) + 1