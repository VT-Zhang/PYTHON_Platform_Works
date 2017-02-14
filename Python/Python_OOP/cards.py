class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print "{} of {}".format(self.value, self.suit)


class Deck(object):
