#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 14:12:09
LastEditTime: 2022-05-02 14:12:09
Description: 
FilePath: 面试题 16.11. 跳水板.py
"""

from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        return [shorter * (k - i) + longer * i for i in range(k + 1)]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.divingBoard(2, 4, 2)
    print(ans)
