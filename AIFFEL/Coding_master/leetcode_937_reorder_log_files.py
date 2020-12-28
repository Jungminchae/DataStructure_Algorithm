from typing import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # let, dig을 구분할 리스트 생성
        temp_let = []
        temp_dig = []
        for log in logs:
            
            temp = log.split()
            temp = ' '.join(temp[1:])
            # identifier 다음에 숫자가 오는지 확인 후 맞으면 dig 아니면 let
            if temp[0].isdigit(): 
                temp_dig.append(log)
            else:
                temp_let.append(log)
        # 정렬
        temp_let.sort()
        temp_let.sort(key = lambda x: x.split()[1:])
        return temp_let + temp_dig

if __name__ == '__main__':
    test = Solution()
    data = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(test.reorderLogFiles(data))