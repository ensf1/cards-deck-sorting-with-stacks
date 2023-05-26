class Stack:
    def __init__(self, head):
        self.head = head
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur) + " -> "
            cur = cur.next
        return out[:-3]

    def isEmpty(self):
        return self.size == 0

    def top(self):
        if self.isEmpty():
            raise Exception("No top, empty stack")
        return self.head.next.suit

    def push(self, node):
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
