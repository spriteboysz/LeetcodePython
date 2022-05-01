#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 23:37:46
LastEditTime: 2022-05-01 23:40:52
Description: 
FilePath: 面试题 17.10. 主要元素.py
"""

from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len(nums) // 2:
                return num
        return -1


if __name__ == "__main__":
    solution = Solution()
    ans = solution.majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])
    print(ans)
    ans = solution.majorityElement([3, 2])
    print(ans)
    ans = solution.majorityElement([2, 1, 1, 1, 2, 2])
    print(ans)
