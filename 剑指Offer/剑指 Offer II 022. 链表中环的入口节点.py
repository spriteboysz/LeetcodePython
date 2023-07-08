#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 22:28
LastEditTime: 2022-06-19 22:28
Description:
FilePath: 剑指 Offer II 022. 链表中环的入口节点.py
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return fast
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
