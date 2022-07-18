import sys
input = sys.stdin.readline

N, M = map(int, input().split())
building = [ input().strip() for _ in range(N)]

row = [0] * N 
col = [0] * M

for i in range(N):
    for j in range(M):
        if building[i][j] == 'X':
            row[i] += 1
            col[j] += 1

result_1 = 0 
for i in range(N):
    if row[i] == 0:
        result_1 += 1

result_2 = 0
for j in range(M):
    if col[j] == 0:
        result_2 += 1

print(max(result_1, result_2))