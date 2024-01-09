#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-09 22:57
FileName: algorithm
Description:P2760. 最长奇偶子数组.py 
"""
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans, n = 0, len(nums)
        for left in range(n):
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                right = left + 1
                while right < n and nums[right] % 2 != nums[right - 1] % 2 and nums[right] <= threshold:
                    right += 1
                ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    print(Solution().longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5))
