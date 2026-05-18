class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_len = 0
        visited = set()

        for i in range(len(nums)):

            # skip if already processed
            if i in visited:
                continue

            s = set()
            curr = i

            while curr not in s:
                s.add(curr)
                visited.add(curr)
                curr = nums[curr]

            max_len = max(max_len, len(s))

        return max_len

        
        

            
        