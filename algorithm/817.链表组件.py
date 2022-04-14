#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 23:39:14
LastEditTime: 2022-04-13 23:40:16
Description: 
FilePath: 817.链表组件.py
"""
#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

# @lc code=start
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count, nums = 0, set(nums)
        while head:
            if head.val in nums:
                if not head.next or head.next.val not in nums:
                    count += 1
            head = head.next
        return count


# @lc code=end
