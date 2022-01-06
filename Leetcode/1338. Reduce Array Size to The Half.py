def minSetSize(arr):

        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        ans = 0
        lenAns = 0
        while ans < len(arr) // 2:
            ans += counts[0][1]
            lenAns += 1
            counts.pop(0)
        
        return lenAns
