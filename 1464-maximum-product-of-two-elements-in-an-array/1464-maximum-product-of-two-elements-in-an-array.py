class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a = nums
        i = a[0]
        j = a[1]
        return (i-1)*(j-1)
        