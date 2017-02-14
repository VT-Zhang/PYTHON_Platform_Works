import random

class Deck(object):
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        suits = ["Club", "Spade", "Heart", "Diamond"]
        faceCards = ["Jack", "Queen", "King", "Ace"]
        for outer_count in range(0, 4):
            for inner_count in range(1, 14):
                if inner_count == 1:
                    card = Card(suits[outer_count], faceCards[3])
                if inner_count == 11:
                    card = Card(suits[outer_count], faceCards[0])
                if inner_count == 12:
                    card = Card(suits[outer_count], faceCards[1])
                if inner_count == 13:
                    card = Card(suits[outer_count], faceCards[2])
                card = Card(suits[outer_count], inner_count)
                self.deck.append(card)

    def shuffleDeck(self):
        random.shuffle(self.deck)
        return self.deck

    def flipCard(self):
        return self.deck.pop()

    def resetDeck(self):
        self.deck = []
        self.creatDeck()

    def deal2Cards(self):
        dealtCards =[]
        for count in range(0, 2)
            dealtCards.append(self.deck.pop())
        return dealtCards


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.suit == "Club" or self.suit == "Spade":
            self.color = "Black"
        else:
            self.color = "Red"

    def __repr__(self):
        return:"Suit: %r Color: %r Value: %r" % (self.suit, self.color, self.value)

deck1 = Deck()
# print deck1.deck[0].suit
# print deck1.deck[0].color
# print deck1.deck[0].value
print deck1
