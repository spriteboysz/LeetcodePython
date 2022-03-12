#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 22:15:15
LastEditTime: 2022-03-12 22:01:52
Description: 
FilePath: 1418.点菜展示表.py
"""
#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        row = defaultdict(lambda: defaultdict(int))
        foods = set()

        for _, table, food in orders:
            row[int(table)][food] += 1
            foods.add(food)
        foods = sorted(foods)
        exhibition = [["Table"] + foods]
        for table in sorted(row.keys()):
            cur = [str(table)]
            for food in foods:
                cur.append(str(row[table][food]))
            exhibition.append(cur)

        return exhibition


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.displayTable(
        [
            ["David", "3", "Ceviche"],
            ["Corina", "10", "Beef Burrito"],
            ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"],
            ["Carla", "5", "Ceviche"],
            ["Rous", "3", "Ceviche"],
        ]
    )
    print(ans)
