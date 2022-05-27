#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 23:38
LastEditTime: 2022-05-27 23:38
Description:
FilePath: LCP 11. 期望个数统计.py
"""

from typing import List


class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
