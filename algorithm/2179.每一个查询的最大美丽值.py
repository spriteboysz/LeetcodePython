#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 22:44:23
LastEditTime: 2022-02-08 22:51:28
Description: 
FilePath: 2179.每一个查询的最大美丽值.py
'''
#
# @lc app=leetcode.cn id=2179 lang=python3
#
# [2070] 每一个查询的最大美丽值
#

# @lc code=start
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        beauty = dict()
        for item in items:
            if item[0] in beauty:
                beauty[item[0]] = max(beauty[item[0]], item[1])
            else:
                beauty[item[0]] = item[1]
        beauty = sorted(beauty.items())
        maximum = []
        for query in queries:
            cur = 0
            for i in range(len(beauty)):
                if query >= beauty[i][0]:
                    cur = max(cur, beauty[i][1])
                else:
                    break
            maximum.append(cur)
        return maximum

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maximumBeauty(items=[[1, 2], [3, 2], [2, 4], [
          5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]))
    print(s.maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], queries=[1]))
    print(s.maximumBeauty(items=[[10, 1000]], queries=[5]))
