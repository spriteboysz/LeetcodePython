#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-17 22:27
LastEditTime: 2022-06-17 22:27
Description:
FilePath: 1343.大小为 K 且平均值大于等于阈值的子数组数目.py
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target, cur, count = k * threshold, sum(arr[:k]), 0
        for i in range(k, len(arr)):
            if cur >= target:
                count += 1
            cur += arr[i]
            cur -= arr[i - k]
        return count + (cur >= target)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numOfSubarrays(
        arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
    print(ans)  # 3
    print(solution.numOfSubarrays(
            arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3],
            k=3,
            threshold=5))
