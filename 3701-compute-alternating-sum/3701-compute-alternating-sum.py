class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        numb = 0
        for i in range(0, len(nums)):
            if i % 2 == 0:
                numb += nums[i]
            else:
                numb -= nums[i]
        return numb


        