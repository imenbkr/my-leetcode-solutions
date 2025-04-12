class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circleStudentCount = students.count(0)
        squareStudentCount = students.count(1)
        
        for sandwich in sandwiches:
            if sandwich == 0:
                if circleStudentCount == 0:
                    return squareStudentCount
                circleStudentCount -= 1
            else:
                if squareStudentCount == 0:
                    return circleStudentCount
                squareStudentCount -= 1
        
        return 0