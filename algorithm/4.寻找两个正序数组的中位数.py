#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            s = nums[mid] + nums[mid - 1]
            return s / 2
        else:
            return nums[mid]
# @lc code=end

