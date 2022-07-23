#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 23:29:54
LastEditTime: 2022-02-17 23:33:48
Description: 
FilePath: 442.数组中重复的数据.py
"""
#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                duplicates.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return duplicates


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print(ans)
