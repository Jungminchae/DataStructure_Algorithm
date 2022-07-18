import sys

input = sys.stdin.readline

N = int(input())
N_list = [ int(input()) for _ in range(N)]

def check(arr):
    temp = arr[0]
    result = 1
    for i in range(1, len(arr)):
        if temp < arr[i]:
            result +=1
            temp = arr[i]
    return result

left = check(N_list)
right = check(N_list[::-1])

print(left)
print(right)