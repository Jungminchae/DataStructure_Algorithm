# 304번 문제

test_matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        needed_part = self.matrix[row1:row2+1]
        total = 0
        for lst in needed_part:
            total += sum(lst[col1:col2+1])
        return total
    
if __name__ == '__main__':
    temp = NumMatrix(test_matrix)
    print(temp.sumRegion(2,1,4,3))