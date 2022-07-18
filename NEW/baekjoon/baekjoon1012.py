import sys
#  Recursion error 발생
'''
input = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result_list = []
T = int(input())

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0) or (ny >= N) or (nx >= M) or (nx < 0) or (visited[ny][nx]):
            continue
        if baechu_location[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny, nx)

for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    visited = [[0] * M for _ in range(N)]
    baechu_location = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        baechu_location[y][x] = 1

    for i in range(N):
        for j in range(M):
            if baechu_location[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                result += 1
    result_list.append(result)
    
for i in result_list:
    print(i)
'''
import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result_list = []
T = int(input())

def bfs(y, x):
    visited[y][x] = 1
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny < 0) or (ny >= N) or (nx >= M) or (nx < 0) or (visited[ny][nx]):
                continue
            if baechu_location[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                baechu_location[ny][nx] == 0
                queue.append((ny, nx))


for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    visited = [[0] * M for _ in range(N)]
    baechu_location = [[0] * M for _ in range(N)]
    x_y = []
    for _ in range(K):
        x, y = map(int, input().split())
        x_y.append((y, x))
        baechu_location[y][x] = 1
    
    for _y, _x in x_y:
        if visited[_y][_x] == 0:
            bfs(_y, _x)
            result += 1
    result_list.append(result)

for i in result_list:
    print(i)



'''
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    visited[x][y] = 1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if array[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                result += 1
    print(result)

'''