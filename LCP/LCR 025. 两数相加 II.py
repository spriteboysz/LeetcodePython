#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 15:27
FileName: LCP
Description:LCR 025. 两数相加 II.py 
"""
from common.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack, stack1, stack2, carry = [], [], [], 0
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            stack.append(carry % 10)
            carry //= 10
        dummy = ListNode(-1)
        cur = dummy
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().addTwoNumbers(ListNode.create("[7,2,4,3]"), ListNode.create("[5,6,4]")))
