#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 17:15
LastEditTime: 2022-06-04 17:15
Description:
FilePath: 剑指 Offer 35. 复杂链表的复制.py
"""

from copy import deepcopy


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return deepcopy(head)
