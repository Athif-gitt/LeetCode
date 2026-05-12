class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        word = ""
        first = s[:k]

        word += first[::-1] + s[k:len(s)]
        return word



        