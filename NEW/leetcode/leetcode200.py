class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[0]*col for _ in range(row)]
        
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        
        result = 0
        
        def dfs(x, y):
            visited[x][y] = 1
    
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (ny < 0) or (ny >= col) or (nx >= row) or (nx < 0) or (visited[nx][ny] == 1):
                    continue
                if grid[nx][ny] == "1" and visited[nx][ny] == 0:
                    dfs(nx, ny)
        if not grid:
            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    dfs(i, j)
                    result += 1
        return result