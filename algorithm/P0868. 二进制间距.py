#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-18 23:22:27
LastEditTime: 2022-01-18 23:42:14
Description: 
FilePath: 868.二进制间距.py
'''
#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start


class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n).replace("0b", "")
        index = [i for i in range(len(binary)) if binary[i] == "1"]
        for i in range(len(index) - 1):
            index[i] = index[i + 1] - index[i]
        return max(index[:-1]) if len(index) >= 2 else 0

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(5))
    print(s.binaryGap(6))
    print(s.binaryGap(8))
