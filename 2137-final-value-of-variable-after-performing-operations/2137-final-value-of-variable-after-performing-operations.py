class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        number = 0
        for x in operations:
            if "++" in x:
                number += 1
            else:
                number -= 1
        return number

        

        
        