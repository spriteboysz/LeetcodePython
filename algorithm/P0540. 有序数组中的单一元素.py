#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-17 23:16:35
LastEditTime: 2022-03-19 15:41:42
Description: 
FilePath: 540.有序数组中的单一元素.py
"""
#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            next_index = mid + 1 if mid % 2 == 0 else mid - 1
            if nums[mid] == nums[next_index]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(ans)
    ans = solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
    print(ans)
