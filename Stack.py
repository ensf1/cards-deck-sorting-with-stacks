class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def size(self):
        return self.__len__()

    def isEmpty(self):
        return len(self._stack) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self._stack[-1]

    def push(self, card):
        self._stack.append(card)

    def pop(self):
        if self.isEmpty():
            return None
        return self._stack.pop()
