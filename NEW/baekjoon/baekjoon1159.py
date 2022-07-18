import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
names = [input().strip()[0] for _ in range(N)]

count_dict = Counter(names)
players = ""

print(count_dict)

for key, value in count_dict.items():
    if value >= 5:
        players += key

if players == "":
    print("PREDAJA")
else:
    players = players.strip()
    players = sorted(players)
    print("".join(players))