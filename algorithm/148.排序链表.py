#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:34:36
LastEditTime: 2022-03-30 23:38:55
Description: 
FilePath: 148.排序链表.py
"""
#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
from typing import Optional
from xml.dom.minicompat import NodeList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes = sorted(nodes, key=lambda el: el.val)
        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return head


# @lc code=end
