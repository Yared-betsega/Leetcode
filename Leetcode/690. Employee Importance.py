"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total = 0
        self.repo = {}
        for employee in employees:
            self.repo[employee.id] = employee
        
        def importance(node):
            if node:
                self.total += node.importance
                for i in node.subordinates:
                    importance(self.repo[i])
        
        for employee in employees:
            if employee.id == id:
                importance(employee)
                return self.total
                
# time and space complexity
# time complexity = O(n+m)
# n = len(employees)
# m = len(no of subordinates)
# space complexity = O(n)
