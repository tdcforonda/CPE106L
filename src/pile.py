class Pile:
    def __init__(self):
        self.pile = [None] * 52
        self.front = 0
        self.end = 0

    def getSize(self):
        return self.end - self.front

    def clear(self):
        self.end = 0
        self.front = 0

    def addCard(self, card):
        self.pile[self.end] = card
        self.end += 1
        return card

    def addCards(self, p):
        while(p.getSize() > 0):
            self.addCard(p.nextCard())

    def nextCard(self):
        if self.front == self.end:
            return None
        card = self.pile[self.front]
        self.front += 1
        return card

    def display(self):
        for i in range(0, self.end):
            print(self.pile[i])
