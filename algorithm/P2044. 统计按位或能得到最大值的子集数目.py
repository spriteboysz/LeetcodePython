#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 18:00
FileName: algorithm
Description:P2044. 统计按位或能得到最大值的子集数目.py 
"""
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = [0]
        for num in nums:
            res += [num | j for j in res]
        return res.count(max(res))


if __name__ == '__main__':
    print(Solution().countMaxOrSubsets(nums=[2, 2, 2]))
