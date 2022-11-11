from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students=deque(students)
        sandwiches=deque(sandwiches)
        
        while len(sandwiches)!=0 and students.count(1-sandwiches[0])!=len(students) :
            if students[0]==sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
        
        return len(students)