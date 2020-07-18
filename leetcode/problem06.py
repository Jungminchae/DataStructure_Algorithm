s = "PAYPALISHIRING"
numRows =  3
class Solution:
    def convert(self, s, numRows) -> str:
        folder = [list() for _ in range(numRows)]
        def func(s, row, idx):
            if row < numRows:
                folder[row].append(s[idx])
        n_row = 0
        n_idx =0
        down_or_up ='down'
        
        if numRows ==1:
            for _ in range(len(s)):
                func(s, n_row, n_idx)
                n_idx +=1
        else:
            for _ in range(len(s)):
                func(s, n_row, n_idx)
                if down_or_up =='down':
                    n_row += 1
                    n_idx += 1       
                elif down_or_up =='up':
                    n_row -=1
                    n_idx +=1
                if n_row == numRows:
                    n_row -= 2
                    down_or_up ='up'
                elif n_row == -1:
                    n_row += 2
                    down_or_up = 'down'
        answer = ''
        for lst in folder:
            for i in lst:
                answer +=i
        return answer
if __name__== '__main__':
    temp = Solution()
    print(temp.convert(s, numRows))