#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 16:23
LastEditTime: 2022-06-12 16:23
Description:
FilePath: 1775.通过最少操作次数使数组的和相等.py
"""

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1

        diff = sum2 - sum1
        cnt = [0] * 6
        for num in nums1:
            cnt[6 - num] += 1
        for num in nums2:
            cnt[num - 1] += 1

        count = 0
        for i in range(5, 0, -1):
            t = cnt[i] * i
            if t >= diff:
                return count + (diff - 1) // i + 1
            else:
                diff -= t
                count += cnt[i]
        return -1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minOperations(
        nums1=[1, 2, 3, 4, 5, 6],
        nums2=[1, 1, 2, 2, 2, 2])
    print(ans)
