import sys
input = sys.stdin.readline

N = int(input())
N_list = [ int(input()) for i in range(N)]

N_list = sorted(N_list)

for  i in N_list:
    print(i)
