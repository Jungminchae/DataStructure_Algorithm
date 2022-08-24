import sys
import heapq


input = sys.stdin.readline
1
N = int(input())
nums = [int(input()) for _ in range(N)]
max_heap = []
result = []

for i in nums:
    if i == 0 and not max_heap:
        result.append(i)
    elif i == 0 and max_heap:
        num = heapq.heappop(max_heap)
        result.append(-num)
    elif i != 0:
        heapq.heappush(max_heap, -i)
        
for i in result:
    print(i)