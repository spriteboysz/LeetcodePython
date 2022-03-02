#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-02 22:17:09
LastEditTime: 2022-03-02 22:18:12
Description: 
FilePath: 2130.链表最大孪生和.py
"""
#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        n = len(nums)
        # print(nums[: n // 2], nums[n // 2 :][::-1])
        return max(map(lambda a, b: a + b, nums[: n // 2], nums[n // 2 :][::-1]))


# @lc code=end
