class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        least_s = min(strs, key=len)

        output = ''
        for i in range(len(least_s)):
            for s in strs:
                if least_s[i] != s[i]:
                    return output
            output += least_s[i]
        return output
            