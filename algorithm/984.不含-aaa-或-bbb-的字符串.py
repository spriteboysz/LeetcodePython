#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 23:33:59
LastEditTime: 2022-03-19 23:36:47
Description: 
FilePath: 984.不含-aaa-或-bbb-的字符串.py
"""
#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a + b > 3:
            if a > b:
                return "aab" + self.strWithout3a3b(a - 2, b - 1)
            elif a < b:
                return "bba" + self.strWithout3a3b(a - 1, b - 2)
            else:
                return "ab" * a
        else:
            return "a" * a + "b" * b


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.strWithout3a3b(1, 2)
    print(ans)
    ans = solution.strWithout3a3b(4, 1)
    print(ans)
