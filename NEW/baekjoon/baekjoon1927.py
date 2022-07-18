import sys
import heapq
input = sys.stdin.readline

N = int(input())
data = [ int(input()) for _ in range(N)]

heap = []
result = []

for i in data:
    if i == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, i)

for i in result:
    print(i)