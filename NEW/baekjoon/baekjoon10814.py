import sys 

input = sys.stdin.readline

N = int(input())
profiles = [ list(input().split()) for _ in range(N) ]

for profile in profiles:
    profile[0] = int(profile[0])

sorted_profiles = sorted(profiles, key=lambda x: x[0])

for i in sorted_profiles:
    print(i[0], i[1])