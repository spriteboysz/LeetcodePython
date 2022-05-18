#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 22:40:21
LastEditTime: 2022-05-18 22:40:21
Description: 
FilePath: 剑指 Offer II 026. 重排链表.py
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from math import ceil


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, point = [], head
        while point:
            nodes.append(point)
            point = point.next
        n = len(nodes)
        nodes[::2], nodes[1::2] = nodes[: ceil(n / 2)], nodes[::-1][: n // 2]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
