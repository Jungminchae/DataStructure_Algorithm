import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
M = int(input())
N_LIST = list(map(int, input().split()))

sorted_list = sorted(N_LIST)
counter_dict = Counter(sorted_list)

result = 0
diff_list = []

for i in sorted_list:
    diff = M - i
    diff_list.append(diff)

    if diff not in N_LIST or i in diff_list:
        continue

    total = counter_dict[i] * counter_dict[diff]
    result += total

print(result)    
