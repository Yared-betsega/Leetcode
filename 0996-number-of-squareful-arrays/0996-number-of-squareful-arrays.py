class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        @cache 
        def binary_search(m):
            l, r = 1, m 
            while l < r:
                mid = (l + r) // 2
                if mid**2 >= m:
                    r = mid
                else:
                    l = mid + 1
            return m == r**2
        
        n = len(nums)
        counter = set()
        stack = []
        visited = set()
        
        for i in range(n):
            stack.append((nums[:i] + nums[i+1:], [nums[i]]))
    
        while stack:
            
            arr, res = stack.pop()
            visited.add((tuple(arr), tuple(res)))
            if len(arr) == 0:
                counter.add(tuple(res))
            for i in range(len(arr)):
                if binary_search(res[-1] + arr[i]):
                    if (tuple(arr[:i] + arr[i+1:]), tuple(res + [arr[i]])) not in visited:
                        stack.append((arr[:i] + arr[i+1:], res + [arr[i]]))
        return len(counter)