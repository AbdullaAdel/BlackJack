#!/usr/bin/env python3
from .cards import Deck
from .players import Dealer, Player

class BlackJack(Deck, Dealer):
    def __init__(self, player_number):
        self.deck = Deck()
        self.deck.shuffle()

        self.dealer = Dealer()
        self.dealer.start_hand(self.deck)
        
        self.players = []
        for i in range(player_number):
            self.players.append(Player(f"Player {i+1}"))
            self.players[i].start_hand(self.deck)
        
        
    def choose_options(self)->int:
        print('Please select an option: ')
        print('1. Hit')
        print('2. Stand\n')
        option = int(input('##:'))
        if option==1  or option == 2:
            return option
        else:
            print('Invalid input')
            return self.choose_options()
    
    def play_again(self):
        print('Would you like to play again?')
        print('1. Yes')
        print('2. No\n')
        option = int(input('##:'))
        if option==1  or option == 2:
            return option
        else:
            print('Invalid input')
            return self.play_again()
    def starting_hand(self):
    
        for player in self.players:
            player.start_hand(self.deck)
        self.dealer.start_hand(self.deck)
        
    def gameplay(self):
        
        for player in self.players:
            print(f"{player.name}'s turn!")
            print('----------------------------')
            print(self.dealer, "\n")
            print(player, "\n")
            while True:
                if player.calculate_score() > 21:
                    print(f'{player.name} busted!\n')
                    player.score = 0
                    break   
                op = self.choose_options()
                if op == 1:
                    player.hit(self.deck)
                    print(player, "\n")
                elif op == 2:
                    print(f"{player.name} stands!, Hope you're happy with your hand!")
                    break
        self.dealer.visibleHand.append(self.dealer.hand.pop())

        self.dealer.dealerTurn(self.deck)
        
        print(f"{self.dealer.name} stands! Lets see who wins!")
        print('----------------------------')
        
        for player in self.players:
            print(self.dealer, "\n")
            print(f"{player.name} has {player.cardname()} with a score of {player.score}\n")
            if player.score > self.dealer.score:
                if player.score == 21 and len(player.hand) == 2:
                    print(f"{player.name} has Blackjack! {player.name} wins!\n")
                else:
                    print(f"{player.name} wins!\n")
            elif player.score < self.dealer.score:
                print(f"{self.dealer.name} wins!\n")
            else:
                print(f"{player.name} and {self.dealer.name} tie!\n")

        print('----------------------------')
        print('Game Over!')

def main():
    player_number = int(input('How many players? \n'))
    bj = BlackJack(player_number)
    bj.gameplay()

main()
    