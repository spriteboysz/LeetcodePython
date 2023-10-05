#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:24
FileName: LCP
Description:LCR 076. 数组中的第 K 个最大元素.py 
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
