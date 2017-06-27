from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])
a = Card(rank='a', suit='1')
b = Card('b', 4)
print(a, b)


class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    # def __getitem__(self, position):
    #     return self.cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck.cards)
# print(deck[1])

# for i,c in enumerate(deck.cards,1):
#     print(i,c)

print(choice(deck.cards))