class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1 = ''
        l2 = ''
        for word in word1:
            l1 += word

        for word in word2:
            l2 += word

        return l1 == l2
        