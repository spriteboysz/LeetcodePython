#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 23:04:52
LastEditTime: 2022-02-10 23:16:07
Description:
FilePath: 357.计算各个位数不同的数字个数.py
"""
#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            count, cur, k = 10, 9, 9
            for _ in range(2, 1 + min(10, n)):
                cur *= k
                k -= 1
                count += cur
            return count

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countNumbersWithUniqueDigits(3))
