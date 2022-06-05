#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 16:41
LastEditTime: 2022-06-05 16:41
Description:
FilePath: 剑指 Offer II 010. 和为 k 的子数组.py
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, pre_sum = 0, 0
        pre_dict = {0: 1}
        for num in nums:
            pre_sum += num
            count += pre_dict.get(pre_sum - k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subarraySum([1, 2, 1, 2, 3], 3)
    print(ans)
