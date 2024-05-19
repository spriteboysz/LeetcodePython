#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 20:28
FileName: algorithm
Description:P0951. 翻转等价二叉树.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))


if __name__ == '__main__':
    root1 = TreeNode.create('[1,2,3,4,5,6,null,null,null,7,8]')
    root2 = TreeNode.create('[1,3,2,null,6,4,5,null,null,null,null,8,7]')
    print(Solution().flipEquiv(root1, root2))
