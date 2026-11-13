class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hm = defaultdict(int)
        # for i in range(len(numbers)):
        #     if hm[target - numbers[i]]:
        #         return [hm[target - numbers[i]], i + 1] 
        #     hm[numbers[i]] = i + 1

        # return []

        left = 0
        right = len(numbers) - 1
        while left < right:
            add = numbers[left] + numbers[right]
            if add == target:
                return [left + 1, right + 1] 
            if add > target:
                right -= 1
            else:
                left += 1
        
        return []
            