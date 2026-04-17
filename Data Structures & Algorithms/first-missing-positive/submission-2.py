class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if temp < len(nums) and temp >= 0:
                if nums[temp] == 0:
                    nums[temp] = -1 * nums[i]
                elif nums[temp] < 0:
                    continue
                else: nums[temp] = -1 * nums[temp]
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
        

        

