#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 23:55:56
LastEditTime: 2022-04-04 00:00:02
Description: 
FilePath: 2181.合并零之间的节点.py
"""
#
# @lc app=leetcode.cn id=2181 lang=python3
#
# [2181] 合并零之间的节点
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes, cur = [], head
        while cur:
            if cur.val == 0:
                nodes.append(cur)
            else:
                nodes[-1].val += cur.val
            cur = cur.next

        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-2].next = None
        return head

# @lc code=end
