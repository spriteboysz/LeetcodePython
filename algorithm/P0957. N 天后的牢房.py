#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-30 23:14
LastEditTime: 2022-05-30 23:14
Description:
FilePath: 957.N 天后的牢房.py
"""

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        record = [cells]
        for _ in range(n):
            next = [0]
            for j in range(1, len(cells) - 1):
                next.append(1 if cells[j - 1] == cells[j + 1] else 0)
            next.append(0)
            if next in record:
                index = record.index(next)
                loop = len(record) - index
                record = record[index:]
                return record[(n - index) % loop]
            record.append(next[:])
            cells = next[:]
        return cells


if __name__ == '__main__':
    solution = Solution()
    ans = solution.prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], n=7)
    print(ans)
