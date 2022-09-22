import random

class gamedeck():
    my_deck = range(52)
    def __init__(self):
        self.deck = list(self.my_deck)
        
    def give_card(self):
        return self.deck.pop(0)
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    