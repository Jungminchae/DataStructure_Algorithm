# 파이썬 알고리즘 인터뷰
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        counter, seen, stack = Counter(s), set(), []
        
        for char in s:
            # 제거할 문자를 하나씩 제거
            # 문자가 하나 밖에 없다면 0 이 될 것
            counter[char] -= 1
            # 이미 본 문자라면 skip
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
            