class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        visited = set([start])
        while queue:
            cur, length = queue.popleft()
            if cur == end:
                return length
            for ch in bank:
                dif = 0
                for i in range(len(cur)):
                    if cur[i] != ch[i]:
                        dif += 1
                if dif == 1 and ch not in visited:
                        queue.append((ch, length + 1))
                        visited.add(ch)
        return -1
            