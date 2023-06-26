#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-02 23:43:16
LastEditTime: 2022-04-02 23:43:43
Description: 
FilePath: 143.重排链表.py
"""
#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
from collections import deque

from common.ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur, queue, nodes = head, deque(), []
        while cur:
            queue.append(cur)
            cur = cur.next
        while queue:
            nodes.append(queue.popleft())
            if queue:
                nodes.append(queue.pop())
        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        print(str(head))

# @lc code=end
