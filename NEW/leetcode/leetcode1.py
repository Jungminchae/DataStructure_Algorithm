class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            needed_num = target - nums[i]
            
            if needed_num in nums[i+1:]:
                index = nums[i+1:].index(needed_num) + i+1
                return [i, index]