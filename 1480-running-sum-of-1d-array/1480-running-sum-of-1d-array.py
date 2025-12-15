class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        total = 0
        for i in range(0, len(nums)):
            total += nums[i]
            sums.append(total)
        return sums
            
            

