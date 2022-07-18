import sys 
input = sys.stdin.readline

N = int(input())
M = [ int(input()) for _ in range(N)]

M = sorted(M)
for i in M:
    print(i)