#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/2 23:01
FileName: algorithm/P2295. 替换数组中的元素.py
Description: 
"""
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        visited = {}
        for a, b in operations[::-1]:
            visited[a] = visited.get(b, b)
        return [visited.get(num, num) for num in nums]


if __name__ == '__main__':
    print(Solution().arrayChange(nums=[1, 2, 4, 6], operations=[[1, 3], [4, 7], [6, 1]]))
