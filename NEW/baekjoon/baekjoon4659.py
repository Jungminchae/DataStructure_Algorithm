import sys 
from collections import deque
from string import ascii_lowercase

input = sys.stdin.readline

results = []
alphabets = list(ascii_lowercase)
passwords = deque()
while True:
    word = input().strip()
    if word == "end":
        break
    passwords.append(word)


def is_vowel(index):
    if index == 0 or index == 4 or index == 8 or index == 14 or index == 20:
        return True
    else:
        return False

while passwords:
    flag = False
    password = passwords.popleft()
    v_count = 0
    l_count = 0
    has_vowel = False
    for i, char in enumerate(password):
        index = alphabets.index(char)
        if is_vowel(index):
            v_count += 1
            l_count = 0
            has_vowel = True

        else:
            v_count = 0
            l_count += 1
        
        if len(password)-1 == i and not has_vowel:
            flag = True

        if v_count == 3 or l_count == 3:
            flag = True
        if i > 0 and password[i-1] == char and char != "e" and char != "o":
            flag = True
        
    if flag:
        results.append(f"<{password}> is not acceptable.")
    else:
        results.append(f"<{password}> is acceptable.")

for i in results:
    print(i)