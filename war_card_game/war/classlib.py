from war import statics
from random import shuffle

class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = int(statics.values[rank])

    def __str__(self):
        return "%s of %s (value %s)"%(self.rank, self.suit, self.value)

class Deck:

    def __init__(self):

        self.all_cards = []

        for s in statics.suits:
            for r in statics.ranks:
                card = Card(r, s)
                self.all_cards.append(card)

    def __len__(self):
        return len(self.all_cards)

    def __str__(self):
        ret = 'THE DECK IS:\n'
        for c in self.all_cards:
            ret += "%s of %s (value %s)\n"%(c.rank, c.suit, c.value)
        return ret

    def push_card(self, index=0):
        if index > len(self.all_cards):
            index = len(self.all_cards)
        return self.all_cards.pop(index)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_cards(self):

        hand_1 = []
        hand_2 = []

        for f in range(0, len(self.all_cards), 2):
            hand_1.append(self.push_card())
            hand_2.append(self.push_card())
        return [hand_1, hand_2]


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return("Player %s has %s cards" % (self.name, len(self.hand)))

    def deal_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)


    def print_hand(self):
        print("Player %s has:"%self.name)
        for f in self.hand:
            print(f)


class Table:

    def __init__(self):
        self.player_1 = []
        self.player_2 = []

    def add_card(self, card, player):

        player = int(player)

        if player == 1:
            if isinstance(card, list):
                self.player_1.extend(card)
            else:
                self.player_1.append(card)

        else:
            if isinstance(card, list):
                self.player_2.extend(card)
            else:
                self.player_2.append(card)

    def check_winner(self):
        if self.player_1[-1].value > self.player_2[-1].value:
            return 1
        elif self.player_1[-1].value < self.player_2[-1].value:
            return 2
        else:
            return 0

    def return_cards(self):
        #return list(zip(self.player_1, self.player_2))
        ret = []
        for f in range(0, len(self.player_1)):
            ret.append(self.player_1[f])
            ret.append(self.player_2[f])

        self.player_1 = []
        self.player_2 = []
        return ret

    def __str__(self):

        out = ''

        for f in range(0, len(self.player_1)):
            out += "Player  1: %s, player 2: %s\n" % (self.player_1[f], self.player_2[f])

        return out

    def print_last_deal(self):
        print("Player  1: %s, player 2: %s, winner: %s" % (self.player_1[-1], self.player_2[-1], self.check_winner()))
