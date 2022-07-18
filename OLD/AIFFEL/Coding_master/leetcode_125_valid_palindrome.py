from typing import *
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for character in s:
            if character.isalnum():
                strs.append(character.lower())
            # deque[a,m,a,n,a,p,l,a,n,a,c,a,n,a,l]
        # print(strs)

        while len(strs) >= 2:
            if strs.popleft() != strs.pop():
                return False
        return True

if __name__ == '__main__':
    test = Solution()
    data = "A man, a plan, a canal: Panama"
    print(test.isPalindrome(data))
