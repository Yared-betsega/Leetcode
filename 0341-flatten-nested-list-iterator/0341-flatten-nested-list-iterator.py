# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = []
        self.flattenList(nestedList, self.flattened_list)
        self.i=0
                
    def flattenList(self, nestedList, flattenedList):
        for nestedInt in nestedList:
            if nestedInt.isInteger():
                flattenedList.append(nestedInt.getInteger())
            else: 
                self.flattenList(nestedInt.getList(), flattenedList)
            
    def next(self) -> int:
        if self.i < len(self.flattened_list):
            num =  self.flattened_list[self.i]
            self.i += 1
            return num
        else:
            return None
        
    def hasNext(self) -> bool:
        return self.i < len(self.flattened_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())