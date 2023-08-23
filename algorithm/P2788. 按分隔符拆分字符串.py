#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-23 00:00
FileName: algorithm
Description:P2788. 按分隔符拆分字符串.py 
"""
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [word for words in list(map(lambda el: el.split(separator), words)) for word
                in words if word != ""]


if __name__ == '__main__':
    print(Solution().splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator="."))
