#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 23:30:37
LastEditTime: 2022-04-03 23:38:56
Description: 
FilePath: 1669.合并两个链表.py
"""
#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        nodes1, nodes2 = [], []
        cur = list1
        while cur:
            nodes1.append(cur)
            cur = cur.next
        cur = list2
        while cur:
            nodes2.append(cur)
            cur = cur.next
        nodes1 = nodes1[:a] + nodes2 + nodes1[b + 1 :]

        head = nodes1[0]
        for i in range(len(nodes1) - 1):
            nodes1[i].next = nodes1[i + 1]
        nodes1[-1].next = None
        return head


# @lc code=end
