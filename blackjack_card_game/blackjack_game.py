from blackjack import classlib

game = True

while game is True:

    house = classlib.House('HOUSE')
    player = classlib.HumanPlayer('Player',0)
    bank = classlib.Bank()
    player_chips = 123

    while not isinstance(player_chips, int) or player_chips < 1:
        try:
            player_chips = int(input('Player\'s chips? '))
        except Exception as err:
            print(err)

    player.chips = player_chips

    #print(new_deck)

    new_round = True

    print('\nNEW GAME\n')

    while new_round:

        #BET
        player.print_chips()
        if player.chips <= 0:
            print('You lost all your chips and your wife will course you!')
            new_round = False
            break
        bet = -1

        while bet < 0 or bet > player.chips:
            try:
                bet = int(input("Enter bet amount or 0 to leave the table: "))
            except Exception as err:
                print(err)
        if bet == 0:
            new_round = False
            game = False
            break

        bank.take_bet(player.bet_chips(bet))


        print('\nShuffle and new deal...\n======================')
        new_deck = classlib.Deck()
        new_deck.shuffle()

        for f in [house, player]:
            f.empty_hand()
            f.add_cards(new_deck.push_card())
            f.add_cards(new_deck.push_card())

            f.print_info()

        play = True
        while play:
            hit_stand = '?'
            while hit_stand not in ['h', 's']:
                hit_stand = input('hit or stand? [h/s]').lower()

                if hit_stand == 'h':
                    player.add_cards(new_deck.push_card())
                    house.print_info()
                    player.print_info()

                    win = classlib.check_win(player)
                    if win == 'house':
                        bank.earn()
                        play = False


                if hit_stand == 's':

                    house.print_info(True)

                    while house.sum_hand() < 17 and house.sum_hand() <=21:
                        print('Dealer\'s deal:')
                        house.add_cards(new_deck.push_card())
                        house.print_info()

                    win = None
                    #win = classlib.check_win(house)
                    win = classlib.check_win(player, house)

                    if win == 'player':
                        player.chips += bank.pay()
                    if win == 'house':
                        bank.earn()
                    if win == 'push':
                        player.chips += bank.push()

                    play = False

    print("U lost %s chips, your total chips is %s. \nBye bye, see U next time!" % (bank.total, player.chips))


