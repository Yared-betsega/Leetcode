class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        ori = []
        queue = deque([changed[0]])
        for i in range(1,len(changed)):
            if not queue or changed[i] < 2 * queue[0]:
                queue.append(changed[i])
            elif changed[i] == 2*queue[0]:
                ori.append(queue.popleft())
            else:
                return []
        return ori if len(ori) == len(changed)/2 else []
            