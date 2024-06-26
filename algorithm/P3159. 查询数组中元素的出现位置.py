#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-26 22:25
FileName: algorithm
Description:P3159. 查询数组中元素的出现位置.py 
"""
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        position = [i for i, num in enumerate(nums) if num == x]
        return [-1 if query > len(position) else position[query - 1] for query in queries]


if __name__ == '__main__':
    print(Solution().occurrencesOfElement(nums=[1, 3, 1, 7], queries=[1, 3, 2, 4], x=1))
