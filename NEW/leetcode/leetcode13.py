from collections import deque

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        result =[]
        s = deque(list(map(lambda x: x, s)))
        
        left = 0 
        right = 1
        
        while len(s) > 1:
            
            if s[left] == "I" and (s[right] =="V" or s[right] =="X"):
                value = roman[s[right]] - roman[s[left]]
                result.append(value)
                s.popleft()
                s.popleft()  
            elif s[left] == "X" and (s[right] =="L" or s[right] =="C"):
                value = roman[s[right]] - roman[s[left]]
                result.append(value)
                s.popleft()
                s.popleft()
            elif s[left] == "C" and (s[right] =="D" or s[right] =="M"):
                value = roman[s[right]] - roman[s[left]]
                result.append(value)
                s.popleft()
                s.popleft()
            else:
                value = roman[s[left]]
                result.append(value)
                s.popleft()
        
        if s:
            result = result + [roman[s[0]]]
        
        answer = sum(result)
        return answer