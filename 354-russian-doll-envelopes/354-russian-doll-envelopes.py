class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        russianDoll = []
        print(envelopes)
        for _, height in envelopes:
            left, right = 0, len(russianDoll) - 1
            while left <= right:
                mid=(left + right) // 1
                if russianDoll[mid] >= height:
                    right = mid - 1
                else:
                    left = mid + 1        
            idx = left
            if idx == len(russianDoll):
                russianDoll.append(height)
            else:
                russianDoll[idx] = height
        return len(russianDoll)