#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-14 23:33:53
LastEditTime: 2022-04-14 23:37:06
Description: 
FilePath: 2095.删除链表的中间节点.py
"""
#
# @lc app=leetcode.cn id=2095 lang=python3
#
# [2095] 删除链表的中间节点
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        fast, slow, cur = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            cur = slow
            slow = slow.next
        cur.next = cur.next.next
        return head


# @lc code=end
