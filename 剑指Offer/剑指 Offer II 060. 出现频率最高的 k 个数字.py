#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-17 23:49:46
LastEditTime: 2022-05-17 23:49:46
Description: 
FilePath: 剑指 Offer II 060. 出现频率最高的 k 个数字.py
"""

from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        return [
            key
            for key, _ in sorted(count.items(), key=lambda el: el[1], reverse=True)[:k]
        ]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
    print(ans)
