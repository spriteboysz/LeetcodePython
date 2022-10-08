#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 22:28
LastEditTime: 2022-05-29 22:28
Description:
FilePath: 147.对链表进行插入排序.py
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.sort(key=lambda el: el.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
