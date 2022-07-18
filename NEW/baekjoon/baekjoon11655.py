import sys
from string import ascii_lowercase, ascii_uppercase

input = sys.stdin.readline
lower = list(ascii_lowercase)
upper = list(ascii_uppercase)


sentence = input()
new_sentence = ""
for letter in sentence:
    if letter in lower:
        index = lower.index(letter)
        if index > 12:
            index = index - 13
        else:
            index = index + 13
        new_sentence += lower[index]
    elif letter in upper:
        index = upper.index(letter)
        if index > 12:
            index = index - 13
        else:
            index = index + 13
        new_sentence += upper[index]
    elif letter.isalpha() is False:
        new_sentence += letter

print(new_sentence)
