class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_str = max_str = ''
        if len(word1) != len(word2):
            min_str = word1 if len(word1) < len(word2) else word2
            max_str = word1 if len(word1) > len(word2) else word2
        else: 
            min_str, max_str = word1, word2
        res = ''
        for i in range(len(min_str)):
            if min_str == word1:
                res += min_str[i] + max_str[i]
            else:
                res += max_str[i] + min_str[i]
        
        return res + max_str[len(min_str):]