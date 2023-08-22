#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 22:58
FileName: algorithm/P2828. 判别首字母缩略词.py
Description: 
"""
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(map(lambda el: el[0], words)) == s


if __name__ == '__main__':
    print(Solution().isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy"))
