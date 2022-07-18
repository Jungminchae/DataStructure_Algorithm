import sys 

input = sys.stdin.readline

N = input().strip()

N = sorted(N, reverse=True)

print(int("".join(N)))