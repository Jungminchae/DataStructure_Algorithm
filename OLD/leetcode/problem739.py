# 파이썬 알고리즘 인터뷰
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높으면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer