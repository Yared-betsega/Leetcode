import heapq as hq
t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    heap = []
    for i in range(len(a)):
        hq.heappush(heap, (a[i], b[i]))

    while heap:
        cur = hq.heappop(heap)
        if cur[0] <= k:
            k += cur[1]
        
    print(k)

#     time and space complexity 
#     time complexity = O(nlog(n))
#     space complexity = O(n)
