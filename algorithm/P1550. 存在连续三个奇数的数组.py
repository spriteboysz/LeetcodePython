#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-04 23:15:24
Description:
FilePath: 1550.存在连续三个奇数的数组.py
"""
#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        lst = []
        for item in arr:
            if item % 2 == 0:
                lst.append("o")
            else:
                lst.append("e")

        return "".join(lst).count("eee") != 0
    
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
    
