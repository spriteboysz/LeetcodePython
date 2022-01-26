#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 23:22:52
LastEditTime: 2022-01-26 23:28:16
Description: 
FilePath: 1331.数组序号转换.py
'''
#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
from json.tool import main
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        serial = []
        sequence = sorted(set(arr))
        for item in arr:
            serial.append(sequence.index(item) + 1)
        return serial


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.arrayRankTransform([40, 10, 20, 30]))
    print(s.arrayRankTransform([100, 100, 100]))
    print(s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
