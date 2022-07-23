#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 23:45:50
LastEditTime: 2022-01-22 23:50:08
Description: 
FilePath: 1925.统计平方和三元组的数目.py
'''
#
# @lc app=leetcode.cn id=1925 lang=python3
#
# [1925] 统计平方和三元组的数目
#

# @lc code=start


class Solution:
    def countTriples(self, n: int) -> int:
        n2 = [i * i for i in range(1, n + 1)]
        count = 0
        for a in n2:
            for b in n2:
                if a + b in n2:
                    count += 1
        return count
# @lc code=end
