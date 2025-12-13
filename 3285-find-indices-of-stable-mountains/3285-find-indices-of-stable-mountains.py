class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        refined = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                refined.append(i)
        return refined
            

        