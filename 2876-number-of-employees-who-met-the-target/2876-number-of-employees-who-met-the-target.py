class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        completed = []
        for hour in hours:
            if hour >= target:
                completed.append(hour)
        return len(completed)

        