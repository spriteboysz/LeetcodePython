#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:25
FileName: algorithm/P2379. 得到 K 个黑块的最少涂色次数.py
Description: 
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = len(blocks)
        for i in range(len(blocks) - k + 1):
            minimum = min(minimum, blocks[i:i + k].count("W"))
        return minimum


if __name__ == '__main__':
    print(Solution().minimumRecolors(blocks="WBBWWBBWBW", k=7))
