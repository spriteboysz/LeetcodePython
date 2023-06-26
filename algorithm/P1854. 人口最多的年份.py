#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 16:38:54
LastEditTime: 2022-01-23 16:46:03
Description:
FilePath: 1854.人口最多的年份.py
"""
#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#

# @lc code=start
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101
        for person in logs:
            for year in range(person[0] - 1950, person[1] - 1950):
                population[year] += 1
        return population.index(max(population)) + 1950

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))
