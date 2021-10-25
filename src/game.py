from player import Player
from pile import Pile
from card import Card
from deck import CardDeck
import time


class Game:
    def __init__(self):
        print("Welcome to Game Of War!")
        self.player1 = Player(input("Enter player 1 name: "))
        self.player2 = Player(input("Enter player 2 name: "))

    def getWinner(self):
        try:
            if self.player1.numCards() > self.player2.numCards():
                return self.player1
            elif self.player1.numCards() < self.player2.numCards():
                return self.player2
            else:
                return None
        except Exception:
            print(Exception)

    def enoughCards(self, n):
        if self.player1.numCards() < n or self.player2.numCards() < n:
            return False
        return True
