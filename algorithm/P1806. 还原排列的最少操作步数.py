#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 23:14:21
LastEditTime: 2022-04-15 23:22:30
Description: 
FilePath: 1806.还原排列的最少操作步数.py
"""


#
# @lc app=leetcode.cn id=1806 lang=python3
#
# [1806] 还原排列的最少操作步数
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        init = [i for i in range(n)]
        cur = init.copy()
        count = 0
        while True:
            count += 1
            arr = []
            for i in range(n):
                if i % 2 == 0:
                    arr.append(cur[i // 2])
                else:
                    arr.append(cur[n // 2 + (i - 1) // 2])
            if arr == init:
                return count
            else:
                cur = arr


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.reinitializePermutation(2)
    print(ans)
    ans = solution.reinitializePermutation(4)
    print(ans)
    ans = solution.reinitializePermutation(6)
    print(ans)
