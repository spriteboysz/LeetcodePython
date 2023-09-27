#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 21:47
FileName: algorithm
Description:P2857. 统计距离为 k 的点对.py 
"""
from typing import List
from collections import Counter


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans = 0
        cnt = Counter()
        for x, y in coordinates:
            for i in range(k + 1):
                ans += cnt[x ^ i, y ^ (k - i)]
            cnt[x, y] += 1
        return ans


if __name__ == '__main__':
    print(Solution().countPairs(coordinates=[[1, 2], [4, 2], [1, 3], [5, 2]], k=5))
    print(Solution().countPairs(coordinates=[[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], k=0))
