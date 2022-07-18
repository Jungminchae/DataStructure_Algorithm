import sys
import random

input = sys.stdin.readline
N = [int(input()) for _ in range(9)]
 
while True:
    selected_list = random.sample(N, k=7)
    total = sum(selected_list)
    if total == 100:
        break

selected_list.sort()

for i in selected_list:
    print(i)
