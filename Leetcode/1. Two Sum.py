class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sample = ''
        substrings = {}
        if len(s)==0:
            return 0
        i = 0
        while i < len(s):
            if s[i] in sample:
                substrings[sample] = len(sample)
                sample = ''
                char = s[i]
                returnIndex = s.index(char)+1
                s = s[returnIndex:]
                i=0
                continue
            sample += s[i]
            i+=1
            if i == len(s):
                substrings[sample] = len(sample)
        sortedSubs = sorted(substrings.items(), key=lambda item: item[1], reverse = True)
        return sortedSubs[0][1]
