import sys

input = sys.stdin.readline

N = int(input())
pattern = input().strip()
files = [ input().strip() for _ in range(N)]
YES = "DA"
NO = "NE"

pattern_list = pattern.split("*")
length_1, length_2 = len(pattern_list[0]), len(pattern_list[1])

for file in files:
    if len(file) < length_1 + length_2:
        print(NO)
        continue
    elif (file[:length_1] == pattern_list[0]) and (file[-length_2:] == pattern_list[-1]):
        print(YES)
    else:
        print(NO)
