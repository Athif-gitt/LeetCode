class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            move = abs(students[i] - seats[i])
            moves += move
        return moves
                
                    

