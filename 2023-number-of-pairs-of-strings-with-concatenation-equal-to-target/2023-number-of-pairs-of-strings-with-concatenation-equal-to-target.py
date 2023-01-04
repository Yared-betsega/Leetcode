class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        def prefixRem(st):
            if len(st) >= len(target):
                return False, ""
            for i in range(len(st)):
                if st[i] != target[i]:
                    return False, ""
            return True, target[len(st):]
            
        def sufixRem(st):
            if len(st) >= len(target):
                return False, ""
            j = len(target) - 1
            for i in range(len(st) - 1, -1, -1):
                if st[i] != target[j]:
                    return False, ""
                j -= 1
            
            return True, target[:len(target) - len(st)]
                
            
        count = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            found, preRem = prefixRem(nums[i])
            if found:
                ans += count[preRem]
            found, sufRem = sufixRem(nums[i])
            if found:
                ans += count[sufRem]
            count[nums[i]] += 1
        return ans
            