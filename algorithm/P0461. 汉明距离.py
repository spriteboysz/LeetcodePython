#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-08 14:39:43
LastEditTime: 2022-01-08 14:57:35
Description:
FilePath: 461.汉明距离.py
"""
#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx, by = bin(x)[2:], bin(y)[2:]
        if len(bx) > len(by):
            bx, by = by, bx
        bx = "0" * (len(by) - len(bx)) + bx
        count = 0
        for i, j in zip(bx, by):
            if int(i) ^ int(j) == 1:
                count += 1
        return count


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(10, 1))
