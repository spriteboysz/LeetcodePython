#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 23:38:38
LastEditTime: 2022-04-05 23:44:56
Description: 
FilePath: 61.旋转链表.py
"""
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        k %= len(nodes)
        nodes = nodes[-k:] + nodes[:-k]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


# @lc code=end
