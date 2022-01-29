#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 23:36:22
LastEditTime: 2022-01-29 23:49:48
Description: 
FilePath: 1013.将数组分成和相等的三个部分.py
'''
#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        div, mod = divmod(sum(arr), 3)
        if mod == 0:
            cur, i = 0, 0
            for item in arr:
                cur += item
                if cur == div:
                    cur = 0
                    i += 1
                    if i == 3:
                        return True
            return False
        else:
            return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]))
