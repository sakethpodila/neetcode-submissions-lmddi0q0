class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0] * 3 
        for i in nums:
            count[i] += 1
        

        p = 0
        for i in range(len(count)):
            while count[i] != 0:
                nums[p] = i
                count[i] -= 1
                p += 1
        
        return nums