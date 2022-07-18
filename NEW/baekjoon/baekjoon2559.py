import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
tempers = list(map(int, input().split()))

result = []

first_sum = 0
for i in range(K):
    first_sum += tempers[i]
result.append(first_sum)


for i in range(N - K):
    result.append(result[i] - tempers[i] + tempers[K+i])
        
print(max(result))
