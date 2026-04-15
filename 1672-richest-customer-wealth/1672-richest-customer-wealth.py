class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []
        for l in accounts:
            sumd = 0
            for n in l:
                sumd += n

            sums.append(sumd)

        maxx = max(sums)
        return maxx

                

        