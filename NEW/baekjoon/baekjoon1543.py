import sys 

input = sys.stdin.readline

string = input().strip()
find = input().strip()

def make_list(string):
    list = []
    for i in range(len(string)):
        list.append(string[i])
    return list

string = make_list(string)
find = make_list(find)
count = 0

i = 0
n = len(string)-len(find)
while n >= i:
    if string[i:len(find)+i] == find:
        count += 1
        i += len(find)
    else:
        i += 1
print(count)