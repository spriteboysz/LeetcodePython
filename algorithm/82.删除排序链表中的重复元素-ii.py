#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-01 23:28:03
LastEditTime: 2022-04-01 23:28:35
Description: 
FilePath: 82.删除排序链表中的重复元素-ii.py
"""
#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
from collections import defaultdict, deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        values, stack = [], []
        valuescount = defaultdict(int)
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        for value in values:
            valuescount[value] += 1

        while head:
            if valuescount[head.val] == 1:
                stack.append(head)
            head = head.next
        if not stack:
            return None
        head = stack[0]
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
        return head


# @lc code=end
