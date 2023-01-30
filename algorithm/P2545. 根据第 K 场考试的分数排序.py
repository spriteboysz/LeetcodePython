#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 22:39
FileName: algorithm/P2545. 根据第 K 场考试的分数排序.py
Description: 
"""
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


if __name__ == '__main__':
    print(Solution().sortTheStudents(score=[[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], k=2))
