class Cards(object):
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen','King']
    suits = ['S','H','C','D']
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    def __init__(self,ranks,suits,card):
        self.rank = self.ranks[int(card/13)]
        self.suit = self.suits[int(card%13)]
        self.val = card
        
    def __str__(self):
        card_str = self.rank + self.suit
        return card_str
        
        def value(self):
            return self.values[self.val%13]
            
    