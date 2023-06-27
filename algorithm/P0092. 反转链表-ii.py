#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 23:50:29
LastEditTime: 2022-04-04 23:54:30
Description: 
FilePath: 92.反转链表-ii.py
"""


#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next

        nodes = nodes[: left - 1] + nodes[left - 1: right][::-1] + nodes[right:]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]

# @lc code=end
