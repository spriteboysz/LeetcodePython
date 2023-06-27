#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-02 22:29:44
LastEditTime: 2022-03-02 22:31:33
Description: 
FilePath: 876.链表的中间结点.py
"""


#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        cur, node = head, head
        while cur:
            length += 1
            cur = cur.next

        length = length // 2
        while length:
            length -= 1
            node = node.next
        return node

# @lc code=end
