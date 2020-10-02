from blackjack import statics
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
            ret += "%s of %s (value %s)\n" % (c.rank, c.suit, c.value)
        return ret

    def push_card(self, index=0):
        if index > len(self.all_cards):
            index = len(self.all_cards)
        return self.all_cards.pop(index)

    def shuffle(self):
        shuffle(self.all_cards)
'''
    def deal_cards(self):

        hand_1 = []
        hand_2 = []

        for f in range(0, len(self.all_cards), 2):
            hand_1.append(self.push_card())
            hand_2.append(self.push_card())
        return [hand_1, hand_2]
'''


class Player:

    def __init__(self):
        self.hand = []

    def sum_hand(self):

        def tmp_value():
            return sum(s.value for s in self.hand)

        hand_value = tmp_value()

        while hand_value > 21:
            hand_value = tmp_value()
            for f in range(0,len(self.hand)):
                if self.hand[f].value == 11:
                    print('>> !ace')
                    hand_value -= 10
                    self.hand[f].value = 1
                    if tmp_value() <= 21:
                        break
            break

        return hand_value

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def empty_hand(self):
        self.hand = []

    def print_hand(self):
        raise Exception("Abstract method")


class HumanPlayer(Player):

    def __init__(self, name, chips=100):
        Player.__init__(self)
        self.name = name
        self.hand = []
        self.chips = chips

    def __str__(self):
            return "%s has %s cards of total value %s" % (self.name, len(self.hand), self.sum_hand())

    def bet_chips(self, amount):
        self.chips -= amount
        return amount

    def print_info(self):
        print("%s has %s cards of total value %s" % (self.name, len(self.hand), self.sum_hand()))
        print("%s's hand:" % self.name)
        for f in self.hand:
            print('  %s' % f)

    def print_chips(self):
            print('%s has %s chips' % (self.name, self.chips))

class House(Player):

    def __init__(self, name):
        Player.__init__(self)
        self.name = name
        self.hand = []

    def __str__(self):
            return "%s has %s cards" % (self.name, len(self.hand))

    def bet_chips(self, amount):
        return amount

    def print_info(self, revealed=False):
        if len(self.hand) == 2 and revealed == False:
            print('%s has %s cards, revealed value is %s' % (self.name, len(self.hand), self.hand[0].value))
            print('  %s' % self.hand[0])
            print('  HIDDEN CARD')
        else:
            print('%s has %s cards of total value %s' % (self.name, len(self.hand), self.sum_hand()))
            for f in self.hand:
                print('  %s' % f)

    def print_chips(self):
        pass


class Bank:

    def __init__(self):
        self.bet = 0
        self.total = 0

    def __str__(self):
        print(self.total)

    def take_bet(self, bet):
        self.bet += bet

    def pay(self, multiplier=2):
        ret = (self.bet * multiplier)
        self.bet = 0
        return ret

    def earn(self):
        self.total += self.bet
        self.bet = 0


    def push(self):
        ret = self.bet
        self.bet = 0
        return ret


#loose functions

def check_win(player=None, house=None):

    if isinstance(player, Player) and player.sum_hand() > 21:
        print("%s BUST!" % (player.name))
        return 'house'

    if  isinstance(house, Player) and house.sum_hand() > 21:
        print("%s BUST!" % (house.name))
        return 'player'

    if isinstance(player, Player) and isinstance(house, Player):
        if  player.sum_hand() > house.sum_hand():
            print("%s WON!" % (player.name))
            return 'player'
        elif house.sum_hand() > player.sum_hand():
            print("%s WON!" % (house.name))
            return 'house'
        else:
            print("PUSH!")
            return 'push'

