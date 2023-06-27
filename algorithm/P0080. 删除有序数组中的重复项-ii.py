#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-01 23:15:02
LastEditTime: 2022-04-01 23:17:59
Description: 
FilePath: 80.删除有序数组中的重复项-ii.py
"""
#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count < 2 or num != nums[count - 2]:
                nums[count] = num
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.removeDuplicates([1, 1, 1, 2, 2, 3])
    print(ans)
    ans = solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
    print(ans)
