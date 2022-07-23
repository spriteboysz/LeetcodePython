#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-17 23:16:35
LastEditTime: 2022-03-19 22:13:38
Description: 
FilePath: 788.旋转数字.py
"""
#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        validset = {"2", "5", "6", "9", "0", "1", "8"}
        specialset = {"0", "1", "8"}

        count = 0
        for i in range(1, n + 1):
            curset = set(str(i))
            if curset.issubset(validset) and not curset.issubset(specialset):
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rotatedDigits(10)
    print(ans)
