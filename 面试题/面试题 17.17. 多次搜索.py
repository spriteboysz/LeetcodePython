#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 23:35
LastEditTime: 2022-06-10 23:35
Description:
FilePath: 面试题 17.17. 多次搜索.py
"""

from typing import List

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        dictionary = {small: [] for small in smalls if small}
        if len(dictionary) == 0:
            return [[]]

        smalls.sort(key=len)
        minimum, maximum = len(smalls[0]), len(smalls[-1])
        for size in range(minimum, maximum + 1):
            for i in range(0, len(big) - size + 1):
                window = big[i:i + size]
                if window in dictionary:
                    dictionary[window].append(i)
        return list(dictionary.values())

if __name__ == '__main__':
    solution = Solution()
    ans = solution.multiSearch(
        big="mississippi", smalls=[
            "is", "ppi", "hi", "sis", "i", "ssippi"])
    print(ans)
