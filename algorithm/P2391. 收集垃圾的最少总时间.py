#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/1 22:57
FileName: algorithm/P2391. 收集垃圾的最少总时间.py
Description: 
"""
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum([len(x) for x in garbage])
        dic = {}
        for i in range(1, len(garbage)):
            for j in garbage[i]:
                dic[j] = i
        presum, cur = [], 0
        for i in travel:
            cur += i
            presum.append(cur)
        for i in dic:
            ans += presum[dic[i] - 1]
        return ans


if __name__ == '__main__':
    print(Solution().garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
