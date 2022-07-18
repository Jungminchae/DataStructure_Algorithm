import sys 
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count

result = []
max_value = -1
for i in range(1, N +1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=" ")