#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-20 23:36:04
LastEditTime: 2022-01-20 23:42:49
Description: 
FilePath: 1009.十进制整数的反码.py
'''
#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            binary = bin(n).replace("0b", "").lstrip("0")
            return 2 ** (len(binary)) - 1 - n

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.bitwiseComplement(7))
    print(s.bitwiseComplement(10))
