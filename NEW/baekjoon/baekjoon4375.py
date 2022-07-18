import sys 

input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    num = 0 
    return_value = 1 
    while True:
        num = num * 10 + 1
        num %= n 
        if num == 0:
            print(return_value)
            break
        return_value += 1