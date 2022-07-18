"""
1. 아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진 탐색

2. 시간복잡도
- M개 입력값 정렬 = O(NlogN)
- M개를 N개중에서 탐색 = O(MlogN)
- 총합 : O((N+M)logN) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""


import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

# 이진탐색 
nums.sort()

def bi_search(start, end, target):
    if start == end:
        if nums[start] == target:
            print(1)
        else:
            print(0)
        return
    mid = (start + end) // 2
    if nums[mid] < target:
        bi_search(mid + 1, end, target)
    else:
        bi_search(start, mid, target)

for each_target in target_list:
    bi_search(0, N-1, each_target)