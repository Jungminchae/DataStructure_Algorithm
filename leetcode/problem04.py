# 4번 문제

nums1 = [1,2]
nums2 = [3]
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend([i for i in nums2])
        nums1 = sorted(nums1)
        length = len(nums1)
        
        if length % 2 != 0:
            median = nums1[length//2]
            return float(median)
        else:
            median = (nums1[length//2] + nums1[length//2 -1 ]) / 2
            return median
        
if __name__== '__main__':
    temp = Solution()
    print(temp.findMedianSortedArrays(nums1, nums2))