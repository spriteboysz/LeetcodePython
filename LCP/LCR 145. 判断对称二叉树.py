#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 20:18
FileName: LCP
Description:LCR 145. 判断对称二叉树.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        def recur(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return recur(p.left, q.right) and recur(p.right, q.left)

        return not root or recur(root.left, root.right)


if __name__ == '__main__':
    print(Solution().checkSymmetricTree(TreeNode.create("[6,7,7,8,9,9,8]")))
