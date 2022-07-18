import sys

input = sys.stdin.readline
A, B, C = list(map(int, input().split()))

def remains(a,b):
    if b == 1:
        return a % C 
    else:
        c = remains(a, b // 2)
        if b % 2 == 0:
            return c * c % C
        else:
            return c * c * a % C
result = remains(A, B)

print(result)
     