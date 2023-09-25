#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 22:37
FileName: 面试题
Description:面试题 10.03. 搜索旋转数组.py 
"""
from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        for i, num in enumerate(arr):
            if num == target:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5))
