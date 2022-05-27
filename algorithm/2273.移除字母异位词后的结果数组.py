#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 21:54
LastEditTime: 2022-05-27 21:54
Description:
FilePath: 2273.移除字母异位词后的结果数组.py
"""

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        anagrams = list(map(lambda el: "".join(sorted(el)), words))
        for i in range(1, len(anagrams)):
            if anagrams[i - 1] == anagrams[i]:
                words[i] = ""
        return list(filter(lambda el: el != "", words))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"])
    print(ans)
