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

    
    def play(self):
        cd = CardDeck()
        cd.shuffle()
        while cd.getSize() >= 2:
            self.player1.collectCard(cd.deal())
            self.player2.collectCard(cd.deal())
        self.player1.useWonPile()
        self.player2.useWonPile()
        down = Pile()

        for t in range(1, 101):
            time.sleep(0.5)
            if(not(self.enoughCards(1))):
                break
            card_1 = Card(None, None)
            card_2 = Card(None, None)
            card_1 = self.player1.playCard()
            card_2 = self.player2.playCard()
            print("\nRound {}:" .format(t))
            print("{}: {}" .format(self.player1.getName(), card_1))
            print("{}: {}" .format(self.player2.getName(), card_2))

            if card_1.compareTo(card_2) > 0:
                self.player1.collectCard(card_1)
                self.player1.collectCard(card_2)
            elif card_1.compareTo(card_2) < 0:
                self.player2.collectCard(card_1)
                self.player2.collectCard(card_2)
            else:
                down.clear()
                down.addCard(card_1)
                down.addCard(card_2)
                done = False

                while done == False:
                    num = card_1.getRank()
                    if not self.enoughCards(num):
                        break
                    print("\nWar! Players put down {} card/s" .format(num))

                    for j in range(1, num+1):
                        card_1 = self.player1.playCard()
                        card_2 = self.player2.playCard()

                    if card_1.compareTo(card_2) > 0:
                        self.player1.collectCards(down)
                        done = True
                    elif card_1.compareTo(card_2) > 0:
                        self.player2.collectCards(down)
                        done = True
            print("{} to {}" .format(self.player1.numCards(), self.player2.numCards()))


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
