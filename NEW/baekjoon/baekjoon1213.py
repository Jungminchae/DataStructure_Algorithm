import sys
from collections import Counter


input = sys.stdin.readline

strs = input().strip()
strs_counter = { k:v for k,v in sorted(Counter(strs).items())}
empty_list = [""] * len(strs)

left = 0
right = len(strs) -1
mid = len(strs) // 2

for k,v in strs_counter.items():
    loop = 1
    if v != 1 and v % 2 == 1:
        loop = v // 2 +1
    elif v % 2 == 0:
        loop = v // 2

    for _ in range(loop):
        if v == 1:
            empty_list[mid] = k
            break
        
        empty_list[left] = k 
        empty_list[right] = k 
        left += 1
        right -= 1
        v -= 2

result_strs = "".join(empty_list)
if result_strs == result_strs[::-1] and len(result_strs) == len(strs):
    print(result_strs)
else:
    print("I'm Sorry Hansoo")