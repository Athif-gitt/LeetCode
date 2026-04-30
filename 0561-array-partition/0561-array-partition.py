class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lst = []
        for i in range(len(nums)):
            if i % 2 == 0:
                lst.append(nums[i])
        return sum(lst)



        