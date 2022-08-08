class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
                    
        
        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums) -1

            if i >0 and nums[i] == nums[i -1]:
                continue
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                    
                elif three_sum < 0:
                    left += 1
                else:
                    answer = [nums[i], nums[left], nums[right]]
                    result.append(answer)
                    
                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1

                    right -=1
                    left +=1
        return result