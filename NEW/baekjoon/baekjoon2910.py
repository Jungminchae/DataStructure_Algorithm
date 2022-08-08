import sys 
from collections import Counter

input = sys.stdin.readline

N, C = map(int, input().split())
N_list = list(map(int, input().split()))

counter_dict = Counter(N_list)

for i,j in counter_dict.most_common():
    for _ in range(j):
        print(i, end=' ')
        