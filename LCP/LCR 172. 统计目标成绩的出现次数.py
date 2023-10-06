#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:22
FileName: LCP
Description:LCR 172. 统计目标成绩的出现次数.py 
"""
from typing import List


class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        return len(list(filter(lambda score: score == target, scores)))


if __name__ == '__main__':
    print(Solution().countTarget(scores=[2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target=4))
