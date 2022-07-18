import sys
input = sys.stdin.readline

def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return 
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n / 2, x, y)
    solve(n / 2, x, y + n /2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n /2, y + n /2) 

N, X, Y = map(int, input().split())
first_location =[]

if X < (2**N) / 2 and Y < (2**N) / 2:
    print("1")
    first_location.append(0) # left
    first_location.append(0) # top
    result = 0
    # solve(2**N, 0, 0) 
elif X >= (2**N) / 2 and Y < (2**N) / 2:
    print("2")
    first_location.append(1) # right
    first_location.append(0) # top
    result = (2**N) / 2 * (2**N) / 2
    # solve(2**N, 0, (2**N) / 2)
elif X < (2**N) / 2 and Y >= (2**N) / 2:
    print("3")
    first_location.append(0) # left
    first_location.append(1) # bottom
    result = (2**N) / 2 * (2**N)
    # solve(2**N, (2**N) / 2, 0)
elif X >= (2**N) / 2 and Y >= (2**N) / 2:
    print("4")
    first_location.append(1) # right
    first_location.append(1) # bottom
    result = ((2**N) * (2**N)) - ((2**N) / 2 * (2**N) / 2)
    # solve(2**N, (2**N) / 2, (2**N) / 2)

if first_location[0] == 0 and first_location[1] == 0:    
    solve((2**N)/ 2, 0, 0)
elif first_location[0] == 1 and first_location[1] == 0:
    solve((2**N) / 2, 0, 0 + (2**N) /2)
elif first_location[0] == 0 and first_location[1] == 1:
    solve((2**N) / 2, 0 + (2**N) / 2, 0)
elif first_location[0] == 1 and first_location[1] == 1:
    solve((2**N) / 2, X + (2**N) /2, 0 + (2**N) /2) 