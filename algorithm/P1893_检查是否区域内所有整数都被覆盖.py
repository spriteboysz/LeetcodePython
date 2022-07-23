#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-01 22:29:51
LastEditTime: 2022-02-01 22:39:01
Description: 
FilePath: 1893.检查是否区域内所有整数都被覆盖.py
'''
#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        section = [0] * 51
        for item in ranges:
            section[item[0]: item[1] + 1] = [1] * (item[1] - item[0] + 1)
        return 0 not in section[left: right + 1]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isCovered([[1, 10], [10, 20]], 21, 21))
