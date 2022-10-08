#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-19 23:19:24
LastEditTime: 2022-04-19 23:19:45
Description: 
FilePath: 201.数字范围按位与.py
"""
#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rangeBitwiseAnd(5, 7)
    print(ans)
