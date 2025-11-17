class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        srt = []
        for i in range(0, len(nums), 1):
            if nums[i] == target:
                return i
            if nums[i] != target:
                srt.append(nums[i])
        srt.insert(0, target)
        srt2 = sorted(srt)
        return srt2.index(target)               


        