#!/usr/bin/env python3

from Game.cards import Deck
from Game.players import Dealer, Player
# from Game.bj import main

def test1():
    deck = Deck()
    deck.shuffle()
    test_deck = []
    for i in range(52):
        test_deck.append(deck.deck.pop())

    assert len(test_deck) == 52

def test2():
    deck = Deck()
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    d = Dealer()
    d.start_hand(deck)
    p1.start_hand(deck)
    p2.start_hand(deck)
    assert len(p1.hand) == 2
    assert len(p2.hand) == 2
    assert len(d.hand) == 2
    
def test3():
    deck = Deck()
    d = Dealer()
    d.start_hand(deck)
    d.dealerTurn(deck)
    assert d.score >= 17
def tests():
    test1()
    test2()