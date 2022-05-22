#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 17:27
LastEditTime: 2022-05-22 17:27
Description:
FilePath: 面试题 08.08. 有重复字符串的排列组合.py
"""


from typing import List
from itertools import permutations


class Solution:
    def permutation(self, s: str) -> List[str]:
        return list(set(["".join(item) for item in permutations(list(s))]))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.permutation("qqe")
    print(ans)
