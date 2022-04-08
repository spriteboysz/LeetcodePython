#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-08 23:22:58
LastEditTime: 2022-04-08 23:26:16
Description: 
FilePath: 1721.交换链表中的节点.py
"""
#
# @lc app=leetcode.cn id=1721 lang=python3
#
# [1721] 交换链表中的节点
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes[k - 1], nodes[-k] = nodes[-k], nodes[k - 1]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


# @lc code=end
