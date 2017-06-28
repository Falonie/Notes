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
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck)
print(deck[2])
# print(deck.cards[1])
print(deck[-5:])

# for i,c in enumerate(deck.cards,1):
#     print(i,c)

print(choice(deck))

# for i, d in enumerate(reversed(deck), 1):
#     print(i, d)

print('\n')
# print([i for i in reversed(deck)])

for i in deck[::]:
    print(i)