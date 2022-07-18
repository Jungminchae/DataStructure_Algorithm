import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
array = [0] * 100001

q = deque([N])
while q:
    v = q.popleft()
    if v == K:
        print(array[v])
        break
    for next in (v-1, v+1, v*2):
        if 0 <= next < 100001 and not array[next]:
            array[next] = array[v] + 1
            q.append(next)