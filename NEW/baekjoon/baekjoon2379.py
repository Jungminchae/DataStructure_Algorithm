import sys


input = sys.stdin.readline
A, B, C = list(map(int, input().split()))
times = [ tuple(map(int, input().split())) for _ in range(3)]

max_val = max([ max(i) for i in times ])
total_list = [0] * max_val

for time in times:
    for i in range(time[0]-1, time[1] -1):
        if i < time[1]:
            total_list[i] +=1

for i in range(len(total_list)):
    if total_list[i] == 1:
        total_list[i] = total_list[i] * A
    elif total_list[i] == 2:
        total_list[i] = total_list[i] * B
    else:
        total_list[i] = total_list[i] * C

print(sum(total_list))