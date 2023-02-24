class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        def decrement():
            dec = 0
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    dec += 1
                    if i == k and tickets[i] == 0:
                        return dec
            return dec
        
        ans = 0
        while tickets[k] > 0:
            ans += decrement()
            
        return ans