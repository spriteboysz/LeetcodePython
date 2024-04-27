#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 13:13
FileName: algorithm
Description:P2899. 上一个遍历的整数.py 
"""
from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans, k = [], [], 0
        for num in nums:
            if num > 0:
                seen.insert(0, num)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans


if __name__ == '__main__':
    print(Solution().lastVisitedIntegers(nums=[1, 2, -1, -1, -1]))
    print(Solution().lastVisitedIntegers(nums=[1, -1, 2, -1, -1]))
