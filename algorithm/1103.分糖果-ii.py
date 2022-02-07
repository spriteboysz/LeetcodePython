#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:06:44
LastEditTime: 2022-02-07 23:18:39
Description: 
FilePath: 1103.分糖果-ii.py
'''
#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        for i in range(1, candies):
            if i * i + i > candies * 2:
                length = i - 1
                break
        people = [i for i in range(1, length + 1)]
        people.append(candies - sum(range(1, length + 1)))
        distribute = [0] * num_people
        for i in range(num_people):
            distribute[i] = sum(people[i::num_people])
        return distribute


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies(10, 3))
