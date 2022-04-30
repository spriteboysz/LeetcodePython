#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 15:35:32
LastEditTime: 2022-02-04 15:47:21
Description: 
FilePath: 100181.整数转换.py
'''
#
# @lc app=leetcode.cn id=100181 lang=python3
#
# [面试题 05.06] 整数转换
#

# @lc code=start


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        count = 0
        a = "0" * (64 - len(bin(abs(A)))) + bin(abs(A)).replace("0b", "")
        b = "0" * (64 - len(bin(abs(B)))) + bin(abs(B)).replace("0b", "")
        for i, j in zip(a, b):
            if i != j:
                count += 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(bin(826966453))
    print(bin(-729934991))
    print(s.convertInteger(826966453, -729934991))
