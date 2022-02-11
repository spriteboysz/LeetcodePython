#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-11 23:05:55
LastEditTime: 2022-02-11 23:08:35
Description: 
FilePath: 1680.连接连续二进制数字.py
'''
#
# @lc app=leetcode.cn id=1680 lang=python3
#
# [1680] 连接连续二进制数字
#

# @lc code=start


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = 1
        for i in range(2, n + 1):
            num = num * 2 ** (len(bin(i)) - 2) + i
            num %= 10 ** 9 + 7
        return num
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.concatenatedBinary(3))
    print(s.concatenatedBinary(12))
