#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-16 22:47:37
LastEditTime: 2022-01-16 22:54:11
Description: 
FilePath: 693.交替位二进制数.py
'''
#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n % 2 == 0:
            n += n // 2 + 1
        else:
            n += n * 2 + 1
        return True if bin(n).count("1") == 1 else False


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.hasAlternatingBits(10))
