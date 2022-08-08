from heapq import heapify
import sys 
import heapq

input = sys.stdin.readline
N = int(input())
N_list = [ int(input()) for _ in range(N)]

heap = [] 
for i in N_list:
    heapq.heappush(heap, i)

result = []
for _ in range(1, N):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a + b
    result.append(c)
    heapq.heappush(heap, c)

print(sum(result))