#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 17:29
FileName: algorithm
Description:P0967. 连续差相同的数字.py 
"""
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(path):
            if len(path) == n:
                paths.append(int(''.join(path)))
                return
            left = int(path[-1]) - k
            right = int(path[-1]) + k
            if right <= 9:
                backtrack(path + str(right))
            if left >= 0 and left != right:
                backtrack(path + str(left))

        paths = []
        for i in range(1, 10):
            backtrack(str(i))
        return paths


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(3, 7))
    print(Solution().numsSameConsecDiff(2, 1))
    print(Solution().numsSameConsecDiff(2, 2))
    print(Solution().numsSameConsecDiff(7, 5))
