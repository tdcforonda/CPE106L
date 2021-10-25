
SUITS = ["", "Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def compareTo(self, obj):
        Cardother = Card(obj.rank, obj.suit)
        thisRank = self.getRank()
        otherRank = Cardother.getRank()
        if thisRank == 1:
            thisRank = 14
        if otherRank == 1:
            otherRank = 14
        return thisRank - otherRank

    def __eq__(self, obj):
        if isinstance(obj, Card):
            otherCard = Card(obj.rank, obj.suit)
            return self.rank == otherCard.rank and self.suit == otherCard.suit
        else:
            return False

    def __str__(self):
        global SUITS
        val = ''
        suitList = SUITS
        if self.rank == 1:
            val = 'Ace'
        elif self.rank == 11:
            val = 'Jack'
        elif self.rank == 12:
            val = 'Queen'
        elif self.rank == 13:
            val = 'King'
        else:
            val = str(self.rank)
        s = "{} of {}" .format(val, suitList[self.suit])
        return s
