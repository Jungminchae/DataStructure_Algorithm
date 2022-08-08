import sys 


input = sys.stdin.readline

N = int(input())
words = [ input().strip() for _ in range(N)]
results = []

for word in words:
    result = ""
    for i, char in enumerate(word):
        if char.isdigit():
            result += char
    
        if not char.isdigit():
            if result != "":
                results.append(int(result))
                result = ""
            else:
                continue

    if result != "":
        results.append(int(result))
results.sort()
for i in results:
    print(i)