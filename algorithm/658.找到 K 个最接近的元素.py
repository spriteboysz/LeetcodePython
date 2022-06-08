#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 22:57
LastEditTime: 2022-06-08 22:57
Description:
FilePath: 658.找到 K 个最接近的元素.py
"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # return sorted(sorted(arr, key=lambda el: (abs(el - x), el))[0:k])
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left + k]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3)
    print(ans)
    ans = solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1)
    print(ans)
