#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 23:20:13
LastEditTime: 2022-04-09 23:28:20
Description: 
FilePath: 23.合并k个升序链表.py
"""
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for node in filter(lambda el: el, lists):
            while node:
                nodes.append(node)
                node = node.next
        if not nodes:
            return
        nodes.sort(key=lambda el: el.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


# @lc code=end
