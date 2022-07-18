import sys
from collections import deque

input = sys.stdin.readline

string = input().strip()
string_deque = deque(string)
is_palindrome = 1

while len(string_deque) > 1:
    if string_deque.popleft() != string_deque.pop():
        is_palindrome = 0
        break

print(is_palindrome)
