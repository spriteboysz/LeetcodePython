#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 00:26
LastEditTime: 2022-06-07 00:26
Description:
FilePath: 面试题 02.05. 链表求和.py
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur, carry = head, 0
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return head.next
