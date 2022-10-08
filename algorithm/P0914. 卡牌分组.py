#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-02 23:10:10
LastEditTime: 2022-02-02 23:25:07
Description: 
FilePath: 914.卡牌分组.py
'''
#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card = dict()
        for item in set(deck):
            card[item] = deck.count(item)
        return reduce(gcd, card.values()) >= 2
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
