#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 20:33:11
LastEditTime: 2022-05-02 20:33:54
Description: 
FilePath: 面试题 10.02. 变位词组.py
"""

from typing import List
from collections import defaultdict
from string import ascii_lowercase as lower


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[lower.index(letter)] += 1
            group[tuple(key)].append(word)
        return list(group.values())


if __name__ == "__main__":
    solution = Solution()
    ans = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)
