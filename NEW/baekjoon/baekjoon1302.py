import sys 
from collections import Counter

input = sys.stdin.readline


N = int(input())
N_list = [ input().strip() for _ in range(N)]

counter = Counter(N_list)

most_common_value = counter.most_common()[0][1]

most_commons = [ i[0] for i in counter.most_common() if i[1] == most_common_value]  
most_commons.sort()

print(most_commons[0])