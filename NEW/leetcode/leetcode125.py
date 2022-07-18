def isPalindrome(s):
    from collections import deque
    
    if s.strip() == '':
        return True
    
    string_deque = deque([ i.lower() for i in s if i.isalnum() ])
    
    while len(string_deque) > 1:
        print(string_deque)
        if string_deque.popleft() != string_deque.pop():
            return False
    return True
