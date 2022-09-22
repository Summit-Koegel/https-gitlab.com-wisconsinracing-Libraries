from Deck_Class import gamedeck
from Hand_Class import Hand

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = Hand()
        self.bet = 0
        self.money = 200
    
    def add_card(self, card, a):
        self.add_card.hand(a)
        
    def action(self):
        return input('Do you wish to Hit or Stay:')
        
    
class Dealer(Player):
    
    def action(self):
        if self.hand.total() < 17:
            return 'Hit'
        if self.hand.total() > 16:
                return 'Stay' 
            
    def start(self,player, card, players):
        deck = gamedeck()
        for i in range (len(players)):
            a = deck.give_card
            player[i].add_card(a) 
            a = deck.give_card
            player[i].add_card(a)
        a = deck.give_card()
        self.add_card(card)
        a = deck.give_card()
        self.add_card(card)#What are you giving the card to in these previous three lines?
        
        done = False
        while not done:
            for i in range (len(self.players)):
                players[i].show()
            self.show()
            
            
            for i in range (len(players)):
                if players[i].action() == 'Hit':
                    a = deck.give_card()
                    player[i].add_card(a)
                else:
                    done = True
                    
                
        while not done:#done instead of not done  
            if self.action == 'Hit':
                a = deck.givecard()
                self.add_card(a)
            
            else:
                done = True
            self.finish(players)
                
            def finish(self,player):
                dealer_total = self.hand.total()
                for i in range(len(self.players)):
                    player_total = player[i].Hand.total()
                    if player_total > 21:
                        print ('Player ', players[i].name, 'Busted with a total of', players[i].hand_total)
                else:
                    if player_total > dealer_total:
                        print ('Player ', player[i].name, 'You Won!')
                    else:
                        print ('Player ', player[i].name, 'You Lost')    