import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
row, col = map(int, input().split())
square = [ list(map(int, input().split())) for _ in range(row) ]
edges = []


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global edges
    if square[y][x] ==1:
        edges.append((y, x))
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0) or (ny >= row) or (nx >= col) or (nx < 0) or (visited[ny][nx]):
            continue
        visited[ny][nx] = 1
        dfs(ny, nx)

count_1 = 0

while sum(map(sum, square)) > 0:
    count_2 = 0
    edges = []
    visited = [[0] * col for _ in range(row)]
    dfs(0,0)
    for y, x in edges:
        if square[y][x] == 1:
            count_2 += 1
    for y, x in edges:
        square[y][x] = 0
    
    count_1 += 1


print(count_1)
print(count_2)