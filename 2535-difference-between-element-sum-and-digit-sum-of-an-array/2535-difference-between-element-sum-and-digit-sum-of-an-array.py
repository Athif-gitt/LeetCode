class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for num in nums:
            a += num
            for digit in str(num):
                b += int(digit)

        return abs(a - b)


        