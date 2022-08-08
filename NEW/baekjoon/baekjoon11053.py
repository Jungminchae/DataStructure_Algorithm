import sys


input = sys.stdin.readline

N = int(input())
dp = [1] * (N)
arr = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))