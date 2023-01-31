#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/30 23:01
FileName: algorithm/P2442. 反转之后不同整数的数目.py
Description: 
"""
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
            s.add(int(str(num)[::-1]))
        return len(s)


if __name__ == '__main__':
    print(Solution().countDistinctIntegers([1, 13, 10, 12, 31]))
