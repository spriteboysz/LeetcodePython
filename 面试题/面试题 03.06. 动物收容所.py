#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-05-02 15:17:09
LastEditTime: 2022-05-02 15:28:21
Description: 
FilePath: 面试题 03.06. 动物收容所.py
'''
#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 15:17:09
LastEditTime: 2022-05-02 15:20:51
Description: 
FilePath: 面试题 03.06. 动物收容所.py
"""

from typing import List
from collections import deque


class AnimalShelf:
    def __init__(self):
        self.cat, self.dog, self.count = deque(), deque(), 1

    def enqueue(self, animal: List[int]) -> None:
        if animal[0] == 0:
            self.cat.append((self.count, animal[1]))
        else:
            self.dog.append((self.count, animal[1]))
        self.count += 1

    def dequeueAny(self) -> List[int]:
        if not self.cat and not self.dog:
            return [-1, -1]
        elif not self.cat:
            return [self.dog.popleft()[1], 1]
        elif not self.dog:
            return [self.cat.popleft()[1], 0]
        elif self.dog[0][0] < self.cat[0][0]:
            return [self.dog.popleft()[1], 1]
        else:
            return [self.cat.popleft()[1], 0]

    def dequeueDog(self) -> List[int]:
        return [self.dog.popleft()[1], 1] if self.dog else [-1, -1]

    def dequeueCat(self) -> List[int]:
        return [self.cat.popleft()[1], 0] if self.cat else [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()

if __name__ == "__main__":
    # ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
    # [[], [[0, 0]], [[1, 0]], [], [], []]
    pass
