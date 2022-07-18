import sys
from collections import Counter
from string import ascii_lowercase


input = sys.stdin.readline
string = input()

alphabet_list = list(ascii_lowercase)
alphabet_dict = { key:0 for key in alphabet_list }

count_dict = Counter(string)

for key in count_dict:
    count = count_dict[key]
    if key in alphabet_dict:
        alphabet_dict[key] = count

for value in alphabet_dict.values():
    print(value, end=' ')
