#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 23:34
LastEditTime: 2022-06-07 23:34
Description:
FilePath: 面试题 17.09. 第 k 个数.py
"""

from heapq import heappop, heappush


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        heap = [1]
        num = 0
        for _ in range(k):
            num = heappop(heap)
            while heap and num == heap[0]:
                heappop(heap)
            heappush(heap, num * 3)
            heappush(heap, num * 5)
            heappush(heap, num * 7)
        return num


if __name__ == '__main__':
    solution = Solution()
    ans = solution.getKthMagicNumber(5)
    print(ans)
