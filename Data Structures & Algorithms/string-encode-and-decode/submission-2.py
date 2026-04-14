class Solution:

    def encode(self, strs: List[str]) -> str:
        de_limit = '#' 
        encoded_string = ''
        for word in strs:
            encoded_string += f'{len(word)}{de_limit}' + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_str_list = []
        i = 0
        encounter = True
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            decoded_str_list.append(s[j + 1: j + 1 + l])
            i = j + 1 + l
        return decoded_str_list