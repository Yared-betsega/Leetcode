class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        binary = [1 if s[i] == "|" else 0 for i in range(len(s))]
        pre = [binary[0]]
        for i in range(1, len(binary)):
            pre.append(pre[-1] + binary[i])
        
        ans = [0] * len(queries)
        for i, (s, e) in enumerate(queries):
            left_candle = -1
            if pre[e] - pre[s] + binary[s] < 2:
                ans[i] = 0
            else:
                if binary[s] == 1:
                    left_candle = s
                else:
                    l, r = s, e
                    while l <= r:
                        m = (l + r) // 2
                        if pre[m] > pre[s]:
                            left_candle = m
                            r = m - 1
                        else:
                            l = m + 1
                if binary[e] == 1:
                    right_candle = e
                else:
                    right_candle = -1
                    l, r = s, e
                    while l < r:
                        m = (l + r) // 2
                        if pre[m] < pre[r]:
                            l = m + 1
                        else:
                            r = m
                    right_candle = r

                ans[i] = (right_candle - left_candle + 1) - (pre[e] - pre[s] + binary[s])
        return ans