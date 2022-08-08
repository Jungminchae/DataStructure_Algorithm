import sys 


input = sys.stdin.readline
N, M = map(int, input().split())
J = int(input())
locations = [ int(input()) for _ in range(J)]
steps = 0
cover = [1,M]

for loc in locations:
    if (cover[0] <= loc <= cover[1]):
        continue
    elif cover[1] < loc:
        move = loc - cover[1]
        steps += move
        cover[0] = cover[0] + move
        cover[1] = cover[1] + move
    elif cover[0] > loc:
        move = cover[0] - loc
        steps += move
        cover[0] = cover[0] - move
        cover[1] = cover[1] - move

print(steps)
