import deck_builder as db

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = tuple()
        self.stack = float()

    def add_card_to_hand(self,card):
        self.hand = self.hand + (card,)
    
    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand
    
    def get_stack(self):
        return self.stack
    
    def set_stack(self, new_stack):
        self.stack = new_stack

class Table:
    def __init__(self, small_blind:float = 0.01 , max_size = 8):
        self.players:list[Player] = []
        self.max_size = max_size
        self.small_blind = small_blind
        self.big_blind = small_blind*2
        self.min_buy_in = small_blind*50
        self.max_buy_in = small_blind*200
    
    def get_players(self):
        return self.players
    
    def add_player(self, new_player: Player, buy_in):
        if len(self.players)+1 <= self.max_size:
            if self.min_buy_in <= buy_in <= self.max_buy_in:
                self.players.append(new_player)
                new_player.set_stack(buy_in)
            elif self.min_buy_in > buy_in:
                print("Buy in smaller than the minimum, buy in: ({} - {})".format(self.min_buy_in, self.max_buy_in))
            elif self.max_buy_in < buy_in:
                print("Buy in larger than the maximum, buy in: ({} - {})".format(self.min_buy_in, self.max_buy_in))
        else:
            print("This table is currently full!")

        

class Dealer:
    def __init__(self, table: Table) -> None:
        self.deck = db.Deck()
        self.table = table
        self.players = self.table.get_players()

    def shuffle_deck(self):
        self.deck.shuffle()

    def deal_cards(self, amount):
        if amount < 1:
            raise ValueError
        if type(amount) != int:
            raise TypeError
        
        cards_dealt = []

        for i in range(0, amount):
            for player in self.players:
                dealt_card = self.deck.cards.pop()
                #print(dealt_card)
                player.add_card_to_hand(dealt_card) 

                cards_dealt.append(dealt_card)
        
        return cards_dealt
