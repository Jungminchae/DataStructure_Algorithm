# 1번 문제

test_input = [2,7,11,15]
test_target = 9

class Solution:
    def twoSum(self, nums, target):
        a=0
        b=0
        for i, j in enumerate(nums):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    a = i
                    b = k
        return [a,b]
    
if __name__ == '__main__':
    temp = Solution()
    print(temp.twoSum(test_input, test_target))