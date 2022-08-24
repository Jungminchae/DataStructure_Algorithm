import sys
import heapq


input = sys.stdin.readline

N = int(input())
result = []
abs_heap = []


for _ in range(N):
    num = int(input())
    if num == 0 and not abs_heap:
        result.append((0, 0))
    elif num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    elif num == 0 and abs_heap:
        ret = heapq.heappop(abs_heap)
        result.append(ret)
        
for i in result:
    print(i[1])