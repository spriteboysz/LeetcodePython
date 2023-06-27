#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 22:46
LastEditTime: 2022-06-08 22:46
Description:
FilePath: 560.和为 K 的子数组.py
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0] = 1
        prefix_sum, count = 0, 0
        for num in nums:
            prefix_sum += num
            count += prefix_sum_dict[prefix_sum - k]
            prefix_sum_dict[prefix_sum] += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subarraySum([1, 2, 3], 3)
    print(ans)
