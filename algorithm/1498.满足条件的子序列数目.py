#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 23:33
LastEditTime: 2022-06-15 23:33
Description:
FilePath: 1498.满足条件的子序列数目.py
"""

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, count = 0, len(nums) - 1, 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return count % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numSubseq(nums=[3, 5, 6, 7], target=9)
    print(ans)
    ans = solution.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12)
    print(ans)
