class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        derrived_sums = n * (n+1) // 2
        actual_sums = sum(nums)
        return derrived_sums-actual_sums
        
        