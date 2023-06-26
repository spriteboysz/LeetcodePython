#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:13:16
LastEditTime: 2022-01-22 23:31:45
Description:
FilePath: 1945.字符串转化后的各位数字之和.py
"""
#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#

# @lc code=start
from functools import reduce
from string import ascii_lowercase


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = [ascii_lowercase.index(letter) + 1 for letter in s]
        nums = "".join(map(str, nums))
        for _ in range(k):
            nums = str(reduce(lambda a, b: int(a) + int(b), str(nums)))
        return int(nums)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.getLucky("leetcode", 2))
