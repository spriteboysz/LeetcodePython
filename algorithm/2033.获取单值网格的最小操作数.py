#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 21:21:14
LastEditTime: 2022-02-20 21:22:39
Description: 
FilePath: 2033.获取单值网格的最小操作数.py
"""
#
# @lc app=leetcode.cn id=2033 lang=python3
#
# [2033] 获取单值网格的最小操作数
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lst = []
        for i in grid:
            lst.extend(i)
        lst.sort()

        mid = lst[len(lst) // 2]
        count = 0
        for v in lst:
            if abs(mid - v) % x:
                return -1
            count += abs(mid - v) // x
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minOperations([[2, 4], [6, 8]], 2)
    print(ans)
