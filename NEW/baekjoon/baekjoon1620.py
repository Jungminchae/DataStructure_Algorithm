import sys

input = sys.stdin.readline
N, M  = list(map(int, input().split()))
pocketmon_num_dict = { str(i+1): input().strip() for i in range(N) }
pocketmon_str_dict = { v:k  for k, v in pocketmon_num_dict.items() }
questions = [ input().strip() for _ in range(M)]

for question in questions:
    if str(question).isdigit():
        print(pocketmon_num_dict[str(question)])
    elif str(question).isalpha():
        print(pocketmon_str_dict[str(question)])
