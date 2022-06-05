#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 23:06
LastEditTime: 2022-06-05 23:06
Description:
FilePath: 剑指 Offer II 078. 合并排序链表.py
"""

from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next

        nodes.sort(key=lambda node: node.val)
        head = cur = ListNode()
        for node in nodes:
            cur.next = node
            cur = cur.next
        cur.next = None
        return head.next
