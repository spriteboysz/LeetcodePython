#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-15 22:54:08
LastEditTime: 2022-01-15 23:05:59
Description: 
FilePath: 599.两个列表的最小索引总和.py
'''
#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersection = list(set(list1) & set(list2))
        index = list(map(lambda el: list1.index(
            el) + list2.index(el), intersection))
        minimum, favorite = min(index), []
        for i, r in zip(index, intersection):
            if i == minimum:
                favorite.append(r)
        return favorite

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], [
          "KFC", "Shogun", "Burger King"]))
