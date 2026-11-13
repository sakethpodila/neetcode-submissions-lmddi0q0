class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = defaultdict(int)
        for i in range(len(numbers)):
            if hm[target - numbers[i]]:
                return [hm[target - numbers[i]], i + 1] 
            hm[numbers[i]] = i + 1

        return []
