import sys 

input = sys.stdin.readline

N,C = map(int, input().split())
N_list = [ int(input()) for _ in range(N)]

N_list.sort()

start = N_list[1] - N_list[0]
end = N_list[-1] - N_list[0]
result = 0
def binary_search(arr, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        now_value = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] >= mid + now_value:
                count +=1
                now_value = arr[i]
        if count >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

binary_search(N_list, start, end)
print(result)