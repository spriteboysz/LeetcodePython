#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 20:32
FileName: LCP
Description:LCR 004. 只出现一次的数字 II.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for k, v in dic.items():
            if v == 1:
                return k


if __name__ == '__main__':
    print(Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 100]))
