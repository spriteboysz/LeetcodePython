#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 23:27:04
LastEditTime: 2022-02-02 23:31:51
Description:
FilePath: 908.最小差值-i.py
"""
#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2 * k, 0)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.smallestRangeI([0, 10], 2))
    print(s.smallestRangeI([1, 3, 6], 3))
