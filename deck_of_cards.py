import random

class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{}.{} ".format(self.value, self.suit)


class Deck():

    def __init__(self):
        self.cards = list()
        self.deck = list()
        count = 13
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(count):
                card = Card(value+1, suit)
                self.cards.append(card)
                self.deck.append(card)

    def __str__(self):
        outstr = ''
        for item in self.deck:
            outstr += str(item)
        return outstr

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, count):
        cards = list()
        if count <= len(self.deck):
            for num in range(count):
                cards.append(self.deck.pop())
        return cards

    def stack(self):
        for card in self.cards:
            self.deck.append(card)


class Hand():

    def __init__(self, cards=None):
        self.cards = cards

    def __str__(self):
        outstr = ''
        for item in self.cards:
            outstr += str(item)
        return outstr

    def build(self, cards):
        self.cards = cards

    def discard(self):
        self.cards = None

    def sort(self):
        pass


class BlackJackHand(Hand):
    pass


def main():
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck)

    print('--')

    my_hand = Hand(my_deck.deal(2))
    print(my_hand)

    print('--')
    pass

if __name__ == "__main__":
    main()

