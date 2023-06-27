#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 22:26:17
LastEditTime: 2022-05-18 22:26:18
Description: 
FilePath: 剑指 Offer II 021. 删除链表的倒数第 n 个结点.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
