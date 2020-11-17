'''
This is the game of War.
1. Two players receive 26 cards.
2. Each player plays one card per turn.
3. The player with the higher card takes both cards.
4. If both cards are equal, War is called. An extra three cards are played.
5. The last cards are compared. The player with the higher card takes all cards

This version is only played by two computer players.
Methods are imported from module_player and module deck_of_cards.
'''
from ModulePackage.player import Player
from ModulePackage.deck_of_cards import Deck

#Global Variables

player_one = Player('One')
player_two = Player('Two')

game_deck = Deck()

game_deck.shuffle()

for i in range(26):
    player_one.add_cards(game_deck.deal_one())
    player_two.add_cards(game_deck.deal_one())

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.player_hand) == 0:
        print('Player 1 out of cards. PLAYER 2 WINS!!')
        game_on = False
        break
    if len(player_two.player_hand) == 0:
        print('Player 2 is out of cards. PLAYER 1 WINS!!')
        break

    #If both players still have cards, game continues

    player_one_played_cards = []
    player_one_played_cards.append(player_one.play_card())

    player_two_played_cards = []
    player_two_played_cards.append(player_two.play_card())

    #Round Logic
    at_war = True

    while at_war:
        if player_one_played_cards[-1].value > player_two_played_cards[-1].value:
            player_one.add_cards(player_one_played_cards)
            player_one.add_cards(player_two_played_cards)
            at_war = False

        elif player_one_played_cards[-1].value < player_two_played_cards[-1].value:
            player_two.add_cards(player_one_played_cards)
            player_two.add_cards(player_two_played_cards)
            at_war = False

        else:
            print('War!')
            #Check to see if each player has enough cards

            if len(player_one.player_hand) < 5:
                print('Player one unable to play war! PLAYER TWO WINS!')
                game_on = False
                break

            elif len(player_two.player_hand) < 5:
                print('Player two unable to play war! PLAYER ONE WINS!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_played_cards.append(player_one.play_card())
                    player_two_played_cards.append(player_two.play_card())
