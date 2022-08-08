import sys 
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N])