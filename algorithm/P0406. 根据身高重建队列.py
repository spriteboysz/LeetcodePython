#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-09 23:47
FileName: algorithm
Description:P0406. 根据身高重建队列.py 
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        for index in sorted(range(len(people)), key=lambda i: (-people[i][0], people[i][1])):
            p = people[index]
            ans[p[1]:p[1]] = [p]
        return ans


if __name__ == '__main__':
    print(Solution().reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
