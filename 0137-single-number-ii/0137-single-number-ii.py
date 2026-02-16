class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ideal_list = 3 * sum(set(nums))
        org_list = sum(nums)
        diff = ideal_list - org_list
        return diff // 2
        

            
                    
                




        