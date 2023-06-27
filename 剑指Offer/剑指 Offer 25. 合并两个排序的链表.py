#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 20:57:36
LastEditTime: 2022-05-01 21:07:48
Description: 
FilePath: 剑指 Offer 25. 合并两个排序的链表.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        nodes = []
        while l1 or l2:
            if not l1:
                nodes.append(l2)
                l2 = l2.next
            elif not l2:
                nodes.append(l1)
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    nodes.append(l1)
                    l1 = l1.next
                else:
                    nodes.append(l2)
                    l2 = l2.next
        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return head
