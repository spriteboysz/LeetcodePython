#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 20:06
FileName: algorithm
Description:P0089. 格雷编码.py 
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2 ** n)]


if __name__ == '__main__':
    print(Solution().grayCode(n=2))
