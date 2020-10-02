from war import classlib
import time

play_game = 'y'

while play_game == 'y':
    new_game = None
    prisoners = -1

    print('\n'*5)
    print('================= NEW GAME =================')

    while new_game not in ['y', 'n']:
        new_game = input('Play new game? (y/n): ').lower()
        if new_game == 'n':
            play_game = 'n'
            break
        else:

            while prisoners not in range(0,10):
                try:
                    prisoners = int(input('prisoners of war? (0 - 10): '))
                except Exception as err:
                    print('Error occured: %s'%err)

            new_deck = classlib.Deck()
            player_1 = classlib.Player("Player 1")
            player_2 = classlib.Player("Player 2")

            new_table = classlib.Table()
            new_deck.shuffle()
            hands = new_deck.deal_cards()

            player_1.hand = hands[0]
            player_2.hand = hands[1]

            #print(player_1, player_2, new_deck)
            #print(len(new_deck))
            #player_1.print_hand()
            #player_2.print_hand()


            while len(player_1.hand) > 0 and len(player_2.hand) > 0:
                print("New deal")
                print(player_1, player_2)
                if len(new_table.player_1) > 0:
                    print('WAR: the table is:')
                    print(new_table)
                    print('Now battle begins!!!')

                new_table.add_card(player_1.deal_card(), 1)
                new_table.add_card(player_2.deal_card(), 2)
                new_table.print_last_deal()
                winner = new_table.check_winner()
                if winner == 0:
                    print("WAR!")
                    print('Betting %s cards as prisoners' % prisoners)
                    for f in range(0,prisoners):
                        new_table.add_card(player_1.deal_card(), 1)
                        new_table.add_card(player_2.deal_card(), 2)
                        #new_table.print_last_deal()
                    #time.sleep(2)
                if winner == 1:
                    player_1.add_cards(new_table.return_cards())
                if winner == 2:
                    player_2.add_cards(new_table.return_cards())

            for player in [player_1, player_2]:
                if len(player.hand) > 0:
                    print("Winner is %s, another player out of cards!"%player.name)


