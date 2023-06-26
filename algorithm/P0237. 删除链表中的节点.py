#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-02 22:12:58
LastEditTime: 2022-03-02 22:15:53
Description:
FilePath: 237.删除链表中的节点.py
"""
#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
# @lc code=end

