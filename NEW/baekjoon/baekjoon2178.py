import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M  = map(int, input().split())
miro = [ [ int(s) for s in input().strip()] for _ in range(N) ]
visited = [ [ 0 for _ in range(M)] for _ in range(N) ]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0) or (ny >= N) or (nx >= M) or (nx < 0) or (miro[ny][nx] == 0):
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = visited[y][x] + 1
        queue.append((ny, nx))

print(visited[N-1][M-1])