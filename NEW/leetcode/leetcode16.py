class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minimum = 10**4
        
        for i in range(len(nums) -2):
            left= i + 1
            right = len(nums) - 1
            while left < right:
                closest = nums[i] + nums[left] + nums[right] - target
                if abs(closest) <= abs(minimum):
                    minimum = closest
                
                if closest == 0:
                    return target
                elif closest < 0:
                    left += 1
                else:
                    right -= 1
        return minimum + target