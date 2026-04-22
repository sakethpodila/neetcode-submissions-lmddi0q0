class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l1 = l2 = 0
        while l2 < len(nums):
            nums[l1] = nums[l2]
            while l2 < len(nums) and nums[l2] == nums[l1]:
                l2 += 1
            l1 += 1

        return l1 
            