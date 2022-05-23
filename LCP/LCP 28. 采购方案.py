#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-23 23:11
LastEditTime: 2022-05-23 23:11
Description:
FilePath: LCP 28. 采购方案.py
"""


from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        count, i, j = 0, 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] <= target:
                count += j - i
                i += 1
            else:
                j -= 1
        return count % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.purchasePlans([2, 5, 3, 5], 6)
    print(ans)
    ans = solution.purchasePlans([2, 2, 1, 9], 10)
    print(ans)
