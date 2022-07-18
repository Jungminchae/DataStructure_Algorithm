import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N_list = list(map(int, input().split()))

N_list = sorted(N_list)

print(N_list[K-1])