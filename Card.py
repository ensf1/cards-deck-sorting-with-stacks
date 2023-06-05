from Suits import Suits
import random


class Card:
    def __init__(self):
        self.suit = Suits(random.randint(1, 4))
        self.value = random.randint(1, 10)

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        return self.value < other.value

    def __le__(self, other):
        if self.value == other.value:
            return self.suit <= other.suit
        return self.value < other.value

    def __gt__(self, other):
        if other and self.value == other.value:
            return self.suit > other.suit
        return other and self.value > other.value

    def __ge__(self, other):
        if self.value == other.value:
            return self.suit >= self.suit
        return self.value > other.value


