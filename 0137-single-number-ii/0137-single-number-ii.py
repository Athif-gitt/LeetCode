class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

        for f in freq:
            if freq[f] == 1:
                return f


            
                    
                




        