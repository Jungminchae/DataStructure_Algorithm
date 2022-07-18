import sys 

input = sys.stdin.readline

N = int(input())
answer = []

def find(x):
    if x == parent[x]:
        return x 
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(N):
    parent = {}
    number = {}
    
    M = int(input())
    for _ in range(M):
        name_1, name_2 = input().split()

        if name_1 not in parent.keys():
            parent[name_1] = name_1
            number[name_1] = 1

        if name_2 not in parent.keys():
            parent[name_2] = name_2
            number[name_2] = 1

        union(name_1, name_2)
        print(parent)
        answer.append(number[find(name_1)])

for i in answer:
    print(i)
