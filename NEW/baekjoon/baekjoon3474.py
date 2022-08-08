import sys

input = sys.stdin.readline

N = int(input())
NUMS = [int(input()) for _ in range(N)]


for num in NUMS:
    result_2 = 0
    result_5 = 0
    num_1 = 2
    while num_1 <= num:
        result_2 += num // num_1
        num_1 *= 2
    num_2 = 5
    while num_2 <= num:
        result_5 += num // num_2
        num_2 *= 5
    print(min(result_5, result_2))