#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 23:52:43
LastEditTime: 2022-02-09 00:02:17
Description: 
FilePath: 2028.找出缺失的观测数据.py
'''
#
# @lc app=leetcode.cn id=2028 lang=python3
#
# [2028] 找出缺失的观测数据
#

# @lc code=start
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        print(total)
        missing = [total // n] * n
        print(missing)
        
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
    print(s.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
    print(s.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
    print(s.missingRolls(rolls=[1], mean=3, n=1))
