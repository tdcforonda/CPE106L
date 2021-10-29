from .card import Card
import random


class CardDeck:
    def __init__(self):
        self.num_cards = 52
        self.deck = [None] * self.num_cards
        self.fill()

    def shuffle(self):
        for next in range(self.num_cards):
            r = self.myRandom(next, self.num_cards - 1)
            Temp = self.deck[next]
            self.deck[next] = self.deck[r]
            self.deck[r] = Temp

    def deal(self):
        if self.num_cards == 0:
            return None
        self.num_cards -= 1
        return self.deck[self.num_cards]

    def getSize(self):
        return self.num_cards

    def fill(self):
        index = 0
        for r in range(1, 14):
            for s in range(1, 5):
                self.deck[index] = Card(r, s)
                index += 1
        self.num_cards = 52

    def CheckDeck(self):
        return self.deck[0]

    def myRandom(self, low, high):
        return int((high + 1 - low) * random.random() + low)
