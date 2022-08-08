class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        how_many = len(nums) / 2
        
        answer = []
        n = 0 
        while how_many:
            min_num = min(nums[n], nums[n+1])
            answer.append(min_num)
            n += 2
            how_many -= 1
        
        return sum(answer)