import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
M, N, K= map(int, input().split())

_map = [ [0] * N for _ in range(M) ]
result = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            _map[y][x] = 1

def dfs(y, x):
    _map[y][x] = 1
    _result = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0) or (ny >= M) or (nx >= N) or (nx < 0) or (_map[ny][nx]):
            continue
        if _map[ny][nx] == 0:
            _result += dfs(ny, nx)
    return _result

for i in range(M):
    for j in range(N):
        if _map[i][j] == 0:
            result.append(dfs(i, j))

result = sorted(result)
print(len(result))
print(*result)