#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 19:54:22
LastEditTime: 2022-04-09 20:00:00
Description: 
FilePath: 2048.下一个更大的数值平衡数.py
"""
#
# @lc app=leetcode.cn id=2048 lang=python3
#
# [2048] 下一个更大的数值平衡数
#

# @lc code=start
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBeautiful(n):
            for k, v in Counter(str(n)).items():
                if int(k) != v:
                    return False
            return True

        while not isBeautiful(n + 1):
            n += 1
        return n + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.nextBeautifulNumber(1)
    print(ans)
    ans = solution.nextBeautifulNumber(3000)
    print(ans)
