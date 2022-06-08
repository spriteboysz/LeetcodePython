#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 23:39
LastEditTime: 2022-06-08 23:39
Description:
FilePath: 930.和相同的二元子数组.py
"""

from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        perfix_sum_dict = defaultdict(int)
        perfix_sum_dict[0] = 1
        perfix_sum, count = 0, 0
        for num in nums:
            perfix_sum += num
            count += perfix_sum_dict[perfix_sum - goal]
            perfix_sum_dict[perfix_sum] += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2)
    print(ans)
    ans = solution.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0)
    print(ans)
