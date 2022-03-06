#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 22:55:46
LastEditTime: 2022-03-06 23:01:25
Description: 
FilePath: 1497.检查数组对是否可以被-k-整除.py
"""
#
# @lc app=leetcode.cn id=1497 lang=python3
#
# [1497] 检查数组对是否可以被 k 整除
#

# @lc code=start
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = [0] * k
        for item in arr:
            remainders[item % k] += 1

        if remainders[0] % 2:
            return False
        for i in range(1, int(k / 2) + 1):
            if remainders[i] != remainders[k - i]:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.canArrange([1, 2, 3, 4, 5, 6], 7)
    print(ans)
