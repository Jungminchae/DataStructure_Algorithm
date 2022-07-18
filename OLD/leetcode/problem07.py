# 7번 문제

test_input = 123

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            minus = x[0]
            x = x[1:]
        if x[-1] =='0':
            x = x[:-1]
        stack = []
        for i in x:
            stack.append(i)
        answer =''
        for _ in range(len(stack)):
            answer += stack.pop()
        try:
            if minus:
                answer = minus + answer
        except:
            pass
        
        if answer =='':
            return 0
        elif int(answer) >=2**31 -1 or int(answer) <= -2**31:
            return 0
        else:
            return int(answer)
        
if __name__== '__main__':
    temp = Solution()
    print(temp.reverse(test_input))