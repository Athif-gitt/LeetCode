class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(i) for v in nums for i in str(v)]
        