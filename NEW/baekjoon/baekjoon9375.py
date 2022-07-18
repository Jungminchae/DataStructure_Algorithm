import sys

input = sys.stdin.readline


N = int(input())
cloth_dict = { i:{} for i in range(N)}
answer = []

for i in range(N):
    M = int(input())
    for _ in range(M):
        name, type = input().split()
        if type in cloth_dict[i].keys():
            cloth_dict[i][type].append(name)
        else:
            cloth_dict[i][type] = [name]
    
for i in range(N):
    test_case = cloth_dict[i]
    _sum = 1
    for key in test_case.keys():
        _sum *= len(test_case[key]) +1
    answer.append(_sum -1)

for i in answer:
    print(i)
