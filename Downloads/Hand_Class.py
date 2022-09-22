from Cards_Class import Cards

class Hand(Cards):
    import Cards_Class
    def __init__(self):
        self.cards = []
        
    def create_cards(self, rank, suit):
        for suit in Hand.suits:
            for rank in Hand.ranks: 
                self.give_card(Hand(rank, suit))
                
    def __str__(self,cards,give_card):
        if self.cards:
            card_str = ""
        for card in self.cards:
            card_str += str(card) + ',' + str(card)
            
    def clear(self):
        self.cards = []
        
    def add_card(self,card):
        self.cards.append(card)
        
    def total(self):
        total = 0
        for i in range(len(self.cards)):
            total += self.cards[i].value()
        if total > 21:
            if self.check_for_ace():
                total -= 10
        return total
        
    def check_for_ace(self):
        for i in range(len(self.cards)):
            if self.cards[i].value() == 11:
                return True
        return False
            
                
            