#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 23:50
LastEditTime: 2022-06-08 23:50
Description:
FilePath: 974.和可被 K 整除的子数组.py
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0] = 1
        prefix_sum, count = 0, 0
        for num in nums:
            prefix_sum += num
            for key in prefix_sum_dict:
                if (prefix_sum - key) % k == 0:
                    count += prefix_sum_dict[key]
            prefix_sum_dict[prefix_sum] += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)
    print(ans)
    ans = solution.subarraysDivByK([5], 9)
    print(ans)
