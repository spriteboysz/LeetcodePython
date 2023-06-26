#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-02-03 22:17:33
Description:
FilePath: 167.两数之和-ii-输入有序数组.py
"""
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#


# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, item in enumerate(numbers):
            if target - item in numbers:
                if target - item == item:
                    return [i + 1, i + 2]
                else:
                    return [i + 1, numbers.index(target - item) + 1]
        return -1

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([2, 3, 4], 6))
    print(s.twoSum([-1, 0], -1))
