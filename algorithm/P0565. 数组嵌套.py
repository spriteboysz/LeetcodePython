#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-12 11:16
FileName: algorithm
Description:P0565. 数组嵌套.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(idx: int) -> int:
            # 走过的位置，环的结尾，返回计算原长度
            if nums[idx] == -1:
                return 0
            # 下一个坐标、标记走过
            nxt, nums[idx] = nums[idx], -1
            return 1 + dfs(nxt)

        #  找从某个坐标出发的最大环
        return max(dfs(i) for i in range(len(nums)))


if __name__ == '__main__':
    print(Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2]))
