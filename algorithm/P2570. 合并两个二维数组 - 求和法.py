#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:14
FileName: algorithm/P2570. 合并两个二维数组 - 求和法.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for i, val in nums1:
            dic[i] += val
        for i, val in nums2:
            dic[i] += val
        return sorted(list(map(list, dic.items())), key=lambda el: el[0])


if __name__ == '__main__':
    print(Solution().mergeArrays(nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]))
