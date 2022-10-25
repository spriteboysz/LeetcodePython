#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:31
FileName: algorithm/P2433. 找出前缀异或的原始数组.py
Description: 
"""
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        array = [pref[0]]
        for i in range(1, len(pref)):
            array.append(pref[i] ^ pref[i - 1])
        return array


if __name__ == '__main__':
    solution = Solution().findArray([5, 2, 0, 3, 1])
    print(solution)
