#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-14 22:08:50
LastEditTime: 2022-01-14 22:29:15
Description: 
FilePath: 190.颠倒二进制位.py
'''
#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start


class Solution:
    def reverseBits(self, n: int) -> int:
        length = len(bin(n)) - 2
        count = 0
        binary = bin(n)[2::][::-1] + "0" * (32 - length)
        for i, v in enumerate(binary):
            count += int(v) * 2 ** (32 - i - 1)
        return count

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
