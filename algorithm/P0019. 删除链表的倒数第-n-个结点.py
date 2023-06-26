#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 23:10:27
LastEditTime: 2022-04-04 23:14:28
Description: 
FilePath: 19.删除链表的倒数第-n-个结点.py
"""


#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next

        if n == 1:
            nodes = nodes[:-1]
        else:
            nodes = nodes[:-n] + nodes[-n + 1:]
        if not nodes:
            return None

        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]

# @lc code=end
