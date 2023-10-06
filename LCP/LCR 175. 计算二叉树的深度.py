#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:10
FileName: LCP
Description:LCR 175. 计算二叉树的深度.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.calculateDepth(root.left), self.calculateDepth(root.right)) + 1


if __name__ == '__main__':
    print(Solution().calculateDepth(TreeNode.create("[1, 2, 2, 3, null, null, 5, 4, null, null, 4]")))
