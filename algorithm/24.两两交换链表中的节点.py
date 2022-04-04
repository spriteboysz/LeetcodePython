#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 23:29:21
LastEditTime: 2022-04-04 23:32:24
Description: 
FilePath: 24.两两交换链表中的节点.py
"""
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        stack, nodes, cur = [], [], head
        while cur:
            if len(stack) < 1:
                stack.append(cur)
            else:
                nodes.append(cur)
                nodes.append(stack.pop())
            cur = cur.next
        if stack:
            nodes.append(stack.pop())

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


# @lc code=end
