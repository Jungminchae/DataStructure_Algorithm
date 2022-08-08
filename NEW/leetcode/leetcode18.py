class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 0번 인덱스 하나 고정해놓고 다음 for문부터 3sum
        nums.sort()
        result = set()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # 3sum
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if four_sum == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result


# 빠른 풀이 정답 - 리트코드에서 가져옴
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         def twoSum(nums,target):
#             res = []
#             lo = 0
#             hi = len(nums) -1
#             while (lo < hi):
#                 curSum = nums[lo] + nums[hi]
#                 if curSum < target:
#                     lo += 1
#                 elif curSum > target:
#                     hi -= 1
#                 else:
#                     res.append([ nums[lo], nums[hi]])
#                     lo += 1
#                     hi -= 1
#                     while lo < hi and nums[lo] == nums[lo - 1]:
#                         lo += 1
#             return res
#         def kSum(nums, target, k):
#             res = []
#             if not nums:
#                 return res
#             average_val = target // k
#             if average_val < nums[0] or nums[-1] < average_val:
#                 return res
#             if k ==2:
#                 return twoSum(nums, target)
#             for i in range(len(nums)):
#                 if i ==0 or nums[i-1] != nums[i]:
#                     for subset in kSum(nums[i+1:], target-nums[i], k-1):
#                         res.append([nums[i]] + subset)
#             return res
        
#         nums.sort()
#         return kSum(nums, target, 4)