class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key = lambda x:x[1]-x[0], reverse = True)
        energy = tasks[0][1]
        remain = tasks[0][1] - tasks[0][0]
       
        for cost, threshold in tasks[1:]:
            if remain < threshold:
                energy += (threshold - remain)
                remain = threshold - cost
            else:
                remain -= cost
                
        return energy