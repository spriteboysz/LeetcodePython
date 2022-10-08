#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 00:06:06
LastEditTime: 2022-02-12 00:14:22
Description: 
FilePath: 1461.检查一个字符串是否包含所有长度为-k-的二进制子串.py
'''
#
# @lc app=leetcode.cn id=1461 lang=python3
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        counts = defaultdict(int)
        for i in range(len(s) - k + 1):
            counts[s[i:i+k]] += 1
            if len(counts) == 2 ** k:
                return True
        return False

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.hasAllCodes("00110", 2))
    print(s.hasAllCodes("0110", 1))
    print(s.hasAllCodes("0110", 2))
    print(s.hasAllCodes("0000000001011100", 4))
    print(s.hasAllCodes("00000000001011100", 3))
