import sys


input = sys.stdin.readline
N = int(input())
locations = [list(map(int, input().split())) for _ in range(N)]

sorted_location = sorted(locations, key=lambda x: (x[0], x[1]))

for location in sorted_location:
    print(location[0], location[1])