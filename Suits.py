from enum import Enum


class Suits(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4
    HEAD = 5

    def __str__(self):
        return self.name
