#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-08 22:17
FileName: algorithm
Description:P0763. 划分字母区间.py 
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        partition = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition


if __name__ == '__main__':
    print(Solution().partitionLabels(s="ababcbacadefegdehijhklij"))
