import sys

input = sys.stdin.readline

N = int(input())

num = 1
count = 0
while True:
    if N >= num:
        N -= num
        num = num + 1
        count += 1
    else:
        num = 1
    
    if N == 0:
        break

print(count)
    