#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 17:57
FileName: algorithm
Description:P2917. 找出数组中的 K-or 值.py 
"""
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(max(nums).bit_length()):
            cnt1 = sum(x >> i & 1 for x in nums)
            if cnt1 >= k:
                cnt |= 1 << i
        return cnt


if __name__ == '__main__':
    print(Solution().findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
