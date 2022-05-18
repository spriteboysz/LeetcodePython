#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:16:34
LastEditTime: 2022-05-18 23:16:35
Description: 
FilePath: 剑指 Offer II 077. 链表排序.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda node: node.val)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
