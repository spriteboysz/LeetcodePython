#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 20:36:04
LastEditTime: 2022-05-01 20:38:35
Description: 
FilePath: 剑指 Offer 18. 删除链表的节点.py
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        cur = head
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        return head
