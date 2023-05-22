from Suits import Suits
import random


class Card:
    def __init__(self):
        self.suit = Suits(random.randint(1, 4))
        self.value = random.randint(1, 10)
        self.next = None

