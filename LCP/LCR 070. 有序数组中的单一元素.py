#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:27
FileName: LCP
Description:LCR 070. 有序数组中的单一元素.py 
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
