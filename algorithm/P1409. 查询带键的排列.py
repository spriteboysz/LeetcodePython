#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 13:57:39
LastEditTime: 2022-03-19 14:02:42
Description: 
FilePath: 1409.查询带键的排列.py
"""
#
# @lc app=leetcode.cn id=1409 lang=python3
#
# [1409] 查询带键的排列
#

# @lc code=start
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        array, process = [i + 1 for i in range(m)], []
        for query in queries:
            process.append(array.index(query))
            array.remove(query)
            array.insert(0, query)
        return process


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.processQueries([3, 1, 2, 1], 5)
    print(ans)
    ans = solution.processQueries([4, 1, 2, 2], 4)
    print(ans)
    ans = solution.processQueries([7, 5, 5, 8, 3], 8)
    print(ans)
