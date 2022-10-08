#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 21:56:13
LastEditTime: 2022-04-15 22:01:45
Description: 
FilePath: 1171.从链表中删去总和值为零的连续节点.py
"""
#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#

# @lc code=start

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        seen = dict()
        dummy, prefix = ListNode(0), 0
        dummy.next = head
        seen[0] = dummy
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next

        head, prefix = dummy, 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next


# @lc code=end
