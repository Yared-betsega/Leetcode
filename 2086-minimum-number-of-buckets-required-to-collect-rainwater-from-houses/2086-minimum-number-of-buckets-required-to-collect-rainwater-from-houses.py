class Solution:
    def minimumBuckets(self, street: str) -> int:
        buckets = set()
        for i in range(len(street)):
            if street[i] == "H":
                if i - 1 in buckets:
                    continue
                if i+1 < len(street) and street[i+1] == ".":
                    buckets.add(i+1)
                elif i-1 >=0 and street[i-1] ==".":
                    buckets.add(i-1)
                else:
                    return -1
        return len(buckets)
                
                