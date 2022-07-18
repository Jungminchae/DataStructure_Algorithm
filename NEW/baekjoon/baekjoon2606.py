import sys 

input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0 

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(v):
    global count
    count += 1
    visited[v] = True
    for next in adj[v]:
        if not visited[next]:
            dfs(next)
dfs(1)
print(count - 1)