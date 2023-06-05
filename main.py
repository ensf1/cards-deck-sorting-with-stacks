from Card import Card
from Stack import Stack
from icecream import ic


def stack_card_sort(stack_to_sort: Stack, asc):
    if stack_to_sort.isEmpty():
        return stack_to_sort
    if stack_to_sort.size() == 1:
        return stack_to_sort
    aux_stack = Stack()
    sorted_stack = Stack()
    while stack_to_sort:
        card = stack_to_sort.pop()
        while sorted_stack and (sorted_stack.top() > card) if asc else (sorted_stack.top() < card):
            stack_to_sort.push(sorted_stack.pop())
        sorted_stack.push(card)
        while aux_stack:
            sorted_stack.push(aux_stack.pop())
    return sorted_stack
    # peek = stack_to_sort.pop()
    # if peek > stack_to_sort.top():
    #     aux = stack_to_sort.pop()
    #     stack_to_sort.push(peek)
    #     stack_to_sort.push(aux)


def stack_card_sort_asc(stack):
    return stack_card_sort(stack, True)


def stack_card_sort_desc(stack):
    return stack_card_sort(stack, False)


def main():
    cards_deck = Stack()
    for i in range(1, 6):
        cards_deck.push(Card())
    print(cards_deck)
    cards_deck = stack_card_sort_asc(cards_deck)
    print(cards_deck)
    print(stack_card_sort_desc(cards_deck))


if __name__ == "__main__":
    main()
