#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-25 23:39
FileName: 面试题
Description:面试题 17.15. 最长单词.py 
"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: (-len(word), word))
        for i in range(len(words)):
            pass  # TODO
        return words[0]


if __name__ == '__main__':
    print(Solution().longestWord(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]))
    print(Solution().longestWord(["b", "a", "c"]))
