#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:29
FileName: LCP
Description:LCR 060. 前 K 个高频元素.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return sorted(dic.keys(), key=lambda el: -dic[el])[:k]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
