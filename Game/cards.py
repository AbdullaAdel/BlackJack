import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.score = {"Ace":11,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}
    def __str__(self):
    # Plot the card like 'Ace of Spades', '2 of Hearts', etc.
        return f"{self.rank} of {self.suit}"
class Deck(Card):
    def __init__(self):
        self.rank = {"A" : "Ace",
                "2" : "Two" , 
                "3" : "Three", 
                "4" : "Four", 
                "5" : "Five", 
                "6" : "Six",
                "7" : "Seven", 
                "8" : "Eight",
                "9" : "Nine",
                "10" : "Ten",
                "J" : "Jack",
                "Q" : "Queen",
                "K" : "King"}

        self.suit = {"S":"Spades", "H":"Hearts", "C":"Cloves" ,"D":"Diamonds"}
        self.deck = []
        self.create_deck()
    def create_deck(self):
        
        for r in self.rank:
            for s in self.suit:
                c = Card(self.rank[r],self.suit[s])
                self.deck.append(c)
        # Initialize deck as a list of 52 cards
        
    
    def shuffle(self):
        # Shuffle the deck. Use the random module for this purpose.
        random.shuffle(self.deck)
    
    def get_card(self):
        card = self.deck.pop(random.randrange(0, len(self.deck)-1))
        return card
    