#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-09 22:39
FileName: algorithm/P0284. 顶端迭代器.py
Description: 
"""


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cur = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        t = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None


if __name__ == '__main__':
    peekingIterator = PeekingIterator([1, 2, 3].__iter__())
    print(peekingIterator.next())  # 返回 1 ，指针移动到下一个元素 [1,2,3]
    print(peekingIterator.peek())  # 返回 2 ，指针未发生移动 [1,2,3]
    print(peekingIterator.next())  # 返回 2 ，指针移动到下一个元素 [1,2,3]
    print(peekingIterator.next())  # 返回 3 ，指针移动到下一个元素 [1,2,3]
    print(peekingIterator.hasNext())  # 返回 False
