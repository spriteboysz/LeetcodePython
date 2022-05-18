#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-17 23:41:30
LastEditTime: 2022-05-17 23:41:31
Description: 
FilePath: 剑指 Offer II 061. 和最小的 k 个数对.py
"""

from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        return sorted(
            [[num1, num2] for num1 in nums1 for num2 in nums2],
            key=lambda el: el[0] + el[1],
        )[:k]
        # pairs = []
        # for num1 in nums1:
        #     for num2 in nums2:
        #         pairs.append([num1, num2])
        # pairs.sort(key=lambda el: el[0] + el[1])
        # return pairs[:k]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
    print(ans)
