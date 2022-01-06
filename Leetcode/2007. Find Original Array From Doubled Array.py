def findOriginalArray(changed):
        if len(changed) % 2 != 0:
            return []
        changed = sorted(changed)
        original = []
        d = {}
        for i in changed:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        i = 0
        while i< len(changed):
            if d[changed[i]] > 0:
                try:
                    original.append(changed[i])
                    d[changed[i]] -= 1
                    if d[changed[i]*2] > 0:
                        d[changed[i]*2] -= 1
                    else:
                        return []
                except KeyError:
                    return []
            i += 1
        return original
