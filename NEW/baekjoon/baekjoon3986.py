import sys

input = sys.stdin.readline
N = int(input())
words = [ input().strip() for _ in range(N) ]

result = 0 

for word in words:
    stack = [] 
    for w in word:
        stack.append(w)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if stack == []:
        result += 1

print(result)
