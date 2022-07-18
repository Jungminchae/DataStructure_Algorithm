# 125번 문제

string = "A man, a plan, a canal: Panama"


from collections import deque
class Solution:
    def isPalindrome(self, s):
        strs = deque()
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # O(1) + O(1)
                return False
        return True

if __name__ == '__main__':
    temp = Solution()
    print(temp.isPalindrome(string))