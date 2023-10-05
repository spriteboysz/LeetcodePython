#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 23:00
FileName: LCP
Description:LCR 120. 寻找文件副本.py 
"""
from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        visited = set()
        for document in documents:
            if document in visited:
                return document
            visited.add(document)
        return -1


if __name__ == '__main__':
    print(Solution().findRepeatDocument(documents=[2, 5, 3, 0, 5, 0]))
