class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recur(nums, target, curr):
            if target == 0:
                result.append(curr)
                return 
            elif target < 0:
                return
            
            for i in range(len(nums)):
                recur(nums[i:], target - nums[i], curr + [nums[i]])
        
        recur(candidates, target, [])
        return result