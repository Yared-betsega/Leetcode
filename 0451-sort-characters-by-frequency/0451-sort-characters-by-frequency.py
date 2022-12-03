class Solution:
    def frequencySort(self, s: str) -> str:
        repo = {}
        for char in s:
            if char in repo:
                repo[char] += 1
            else:
                repo[char] = 1
        charFreq = list(repo.items())
        heap = []
        for i in charFreq:
            heapq.heappush(heap, [-1 * i[1], i[0]])
        
        sortedList = []
        for i in range(len(heap)):
            temp = heapq.heappop(heap)
            chars = [temp[1]] * (-1 * temp[0])
            sortedList.extend(chars)
        return "".join(sortedList)
        
            
        print(repo)