class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaderboard = []
        
        cur, repo = persons[0], {}
        for i in persons:
            if i in repo:
                repo[i] += 1
            else:
                repo[i] = 1
            if repo[i] >= repo[cur]:
                self.leaderboard.append(i)
                cur = i
            else:
                self.leaderboard.append(cur)

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        while left <= right:
            if self.times[left] > t:
                break
            mid = (left + right) // 2
            if self.times[mid] > t:
                right = mid - 1
            elif self.times[mid] < t:
                left = mid + 1
            else:
                break
        
        return self.leaderboard[mid]
            
# space and time complexity
# For the initialization  
# time comlexity = O(n), n == len(persons)
# space complexity = O(n)
# for the q function
# time comlexity = O(log(n)),  n == len(times)
# space complexity = O(1)
