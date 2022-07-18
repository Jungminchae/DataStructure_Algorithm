def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    max_len = 1
    start = 0
    for i in range(len(s)):
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]

    # 책 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left +1:right -1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) -1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result