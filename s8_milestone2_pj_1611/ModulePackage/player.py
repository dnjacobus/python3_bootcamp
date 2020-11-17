'''
Single class to create a player.
'''
class Player:
    '''
    This class creates a player object. Allows "player" to hold, play, and add cards.
    '''
    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def play_card(self):
        '''
        Removes first card object of hand to be played.
        '''
        return self.player_hand.pop(0)

    def add_cards(self, new_cards):
        '''
        Adds one card object through append. Adds multiple card objects in a list through extend.
        '''
        if type(new_cards) == type([]):
            self.player_hand.extend(new_cards)
        else:
            self.player_hand.append(new_cards)

    def __str__(self):
        '''
        Displays player name and number of card objects in player hand.
        '''
        return 'Player {} has {} cards.'.format(self.name, len(self.player_hand))