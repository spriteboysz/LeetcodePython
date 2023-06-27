#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-08 22:26:09
LastEditTime: 2022-04-08 22:31:07
Description: 
FilePath: 25.k-个一组翻转链表.py
"""
#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        for i in range(0, len(nodes), k):
            if i + k > len(nodes):
                break
            nodes[i: i + k] = nodes[i: i + k][::-1]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]

# @lc code=end
