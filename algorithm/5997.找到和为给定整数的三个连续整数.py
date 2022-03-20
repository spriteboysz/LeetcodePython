#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 14:41:25
LastEditTime: 2022-03-20 14:42:42
Description: 
FilePath: 5997.找到和为给定整数的三个连续整数.py
"""
#
# @lc app=leetcode.cn id=5997 lang=python3
#
# [5997] 找到和为给定整数的三个连续整数
#

# @lc code=start
from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        div, mod = divmod(num, 3)
        return [div - 1, div, div + 1] if mod == 0 else []


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sumOfThree(33)
    print(ans)
