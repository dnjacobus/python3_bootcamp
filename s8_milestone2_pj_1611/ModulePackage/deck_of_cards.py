'''
Classes with methods to create a deck of cards. 
'''
#Global Variables
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    '''
    Class to create a single card.
    '''
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    '''
    Class to create a deck of 52 unique cards.
    '''
    def __init__(self):

        self.full_deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.full_deck.append(created_card)

    def shuffle(self):
        '''
        Shuffles deck.
        '''
        random.shuffle(self.full_deck)

    def deal_one(self):
        '''
        Deals one card from deck. Removes the object from full_deck.
        '''
        return self.full_deck.pop()