from Card import Card
from Stack import Stack


cards_deck = Stack(Card())
for i in range(1, 6):
    cards_deck.push(Card())
print(cards_deck)

