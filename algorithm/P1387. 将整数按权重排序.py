#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-07 22:52:58
LastEditTime: 2022-04-07 22:55:16
Description: 
FilePath: 1387.将整数按权重排序.py
"""


#
# @lc app=leetcode.cn id=1387 lang=python3
#
# [1387] 将整数按权重排序
#

# @lc code=start
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def weight(num):
            count = 0
            while num != 1:
                count += 1
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
            return count

        return sorted(range(lo, hi + 1), key=weight)[k - 1]


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ans = solution.getKth(12, 15, 2)
    print(ans)
    ans = solution.getKth(1, 1, 1)
    print(ans)
    ans = solution.getKth(10, 20, 5)
    print(ans)
    ans = solution.getKth(1, 1000, 777)
    print(ans)
