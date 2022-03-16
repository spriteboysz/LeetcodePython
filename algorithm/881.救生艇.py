#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 21:03:29
LastEditTime: 2022-03-15 21:05:52
Description: 
FilePath: 881.救生艇.py
"""
#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, count = 0, len(people) - 1, 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numRescueBoats(people=[3, 5, 3, 4], limit=5)
    print(ans)
