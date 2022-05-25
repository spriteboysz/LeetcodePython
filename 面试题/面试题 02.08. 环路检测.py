#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 22:27
LastEditTime: 2022-05-25 22:27
Description:
FilePath: 面试题 02.08. 环路检测.py
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return
