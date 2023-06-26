#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-13 22:02:21
LastEditTime: 2022-02-13 22:25:00
Description:
FilePath: 264.丑数-ii.py
"""
#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count, num = 1, 1
        while count < n:
            i = num + 1
            for item in [2, 3, 5]:
                while i % item == 0:
                    i //= item
            if i == 1:
                count += 1
            num += 1
        return num

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [10, 1, 444, 1690]
    for i, args in enumerate(arguments):
        print("=== *{:02d} INPUT* ===".format(i + 1))
        print(args)
        print("=== *DEBUG* ===")
        answer = solution.nthUglyNumber(args)
        print("=== *{:02d} OUTPUT* ===".format(i + 1))
        print(answer)
