#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 23:49:32
LastEditTime: 2022-04-05 23:52:18
Description: 
FilePath: 141.环形链表.py
"""
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# @lc code=end
