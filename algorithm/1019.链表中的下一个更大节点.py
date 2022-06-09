#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-09 22:47
LastEditTime: 2022-06-09 22:47
Description:
FilePath: 1019.链表中的下一个更大节点.py
"""

from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        value, node = [], head
        while node:
            value.append(node.val)
            node = node.next

        stack = []
        result = [0] * len(value)
        for i in range(len(value)):
            while stack and value[stack[- 1]] < value[i]:
                result[stack.pop()] = value[i]
            stack.append(i)
        return result
