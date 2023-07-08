#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 20:47:38
LastEditTime: 2022-05-01 20:47:39
Description: 
FilePath: 剑指 Offer 24. 反转链表.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.reverse()
        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return head
