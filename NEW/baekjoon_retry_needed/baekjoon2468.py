import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
area = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [0] * N for _ in range(N) ]
check = [ [0] * N for _ in range(N) ]
result = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]



# def dfs(y, x):
#     visited[y][x] = 1
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if (ny < 0) or (ny >= N) or (nx >= N) or (nx < 0):
#             continue
#         if visited[ny][nx] == 0 and check[ny][nx] == 0:
#             dfs(ny, nx)

# for n in range(1, 101):
#     temp = 0
#     for i in range(N):
#         for j in range(N):
#             if area[i][j] <= n:
#                 check[i][j] = 1 # 물에 잠김

#     for i in range(N):
#         for j in range(N):
#             if check[i][j] == 0 and visited[i][j] == 0:
#                 dfs(i, j)
#                 temp += 1
#                 print(temp)
