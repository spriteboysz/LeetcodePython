#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 20:19:46
LastEditTime: 2022-04-09 20:21:16
Description: 
FilePath: 2074.反转偶数长度组的节点.py
"""
#
# @lc app=leetcode.cn id=2074 lang=python3
#
# [2074] 反转偶数长度组的节点
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        i, n, cur_len = 0, len(nodes), 1
        while i < n:
            # cur = nodes[i : min(i + cur_len, n)]
            if min(cur_len, n - i) % 2 == 0:
                nodes[i : min(i + cur_len, n)] = nodes[i : min(i + cur_len, n)][::-1]
            i += cur_len
            cur_len += 1

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


# @lc code=end
