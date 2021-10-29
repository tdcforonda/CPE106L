from pile import Pile

class Player:

    def __init__(self, name):
        self.name = name
        self.playPile = Pile()
        self.wonPile = Pile()

    def playCard(self):
        if self.playPile.getSize() == 0:
            self.useWonPile()
        if self.playPile.getSize() > 0:
            return self.playPile.nextCard()
        return None

    def getName(self):
        return self.name

    def collectCard(self, card):
        self.wonPile.addCard(card)

    def collectCards(self, pile):
        self.wonPile.addCards(pile)

    def useWonPile(self):
        self.playPile.clear()
        self.playPile.addCards(self.wonPile)
        self.wonPile.clear()

    def numCards(self):
        return self.playPile.getSize() + self.wonPile.getSize()
