from Game.cards import Deck
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        
    def start_hand(self, deck):
        for i in range(2):
            self.hand.append(deck.get_card())
        self.calculate_score()


    def hit(self, deck):
        self.hand.append(deck.get_card())
        
    def calculate_score(self):
        self.score = 0
        for card in self.hand:
            self.score += card.score[card.rank]
        if self.score > 21:
            for card in self.hand:
                if card.rank == "Ace":
                    self.score -= 10
                    if self.score <= 21:
                        break
        return self.score
    
    def cardname(self)->str:
        cards = ' | '
        for i in self.hand:
            cards = cards + str(i) + ' | '
        return cards
    
    def stand(self):
        return False
    def __str__(self)->str:
        return f"{self.name} has {self.cardname()} with a score of {self.calculate_score()}"


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        self.hand = []
        self.score = 0
        self.visibleHand = []
        
    def start_hand(self, deck):
        for i in range(2):
            self.hand.append(deck.get_card())
        self.visibleHand.append(self.hand[0])
        self.calculate_score()
    def calculate_score(self)->int:
        self.score = 0
        for card in self.visibleHand:
            self.score += card.score[card.rank]
        if self.score > 21:
            for card in self.visibleHand:
                if card.rank == "Ace":
                    self.score -= 10
                    if self.score <= 21:
                        break
        return self.score
        
    def __str__(self) -> str:
        return f"{self.name} has {self.cardname()} with a score of {self.calculate_score()}"
        
    def dealerTurn(self, deck):
        x = self.calculate_score()
        if  x >= 17:
            return x
        else:
            self.visibleHand.append(self.hand.pop())
            self.hit(deck)
            return self.dealerTurn(deck)
            
    
    def cardname(self)->str:
        cards = ' | '
        for i in self.visibleHand:
            cards = cards + str(i) + ' | '
        return cards
                
        
    