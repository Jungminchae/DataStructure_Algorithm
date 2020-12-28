from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s

if __name__ == '__main__':
    test = Solution()
    data = ["h","e","l","l","o"]
    print(test.reverseString(data))