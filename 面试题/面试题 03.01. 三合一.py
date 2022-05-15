class TripleInOne:
    def __init__(self, stackSize: int):
        self.stack = [[], [], []]
        self.size = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) < self.size:
            self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.stack[stackNum]:
            return self.stack[stackNum].pop()
        return -1

    def peek(self, stackNum: int) -> int:
        if self.stack[stackNum]:
            return self.stack[stackNum][-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stack[stackNum]) == 0
