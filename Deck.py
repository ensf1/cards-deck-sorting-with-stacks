import random

from Card import Card


class Deck:
    def __init__(self):
        self.head = Card()
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + " of " + str(cur.suit) + " -> "
            cur = cur.next
        return out[:-3]

    def isEmpty(self):
        return self.size == 0

    def top(self):
        if self.isEmpty():
            raise Exception("No top, empty stack")
        return self.head.next.suit

    def push(self):
        card = Card()
        card.next = self.head.next
        self.head.next = card
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
