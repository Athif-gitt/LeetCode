class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        b = nums[::-1]
        a = nums + b
        return a
        