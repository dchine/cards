from random import shuffle



class Rank:
    __ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value) -> None:
        if value not in self.__ranks:
            raise ValueError
        self.value = value
        self.numeric_value = int(self.__ranks.index(self.value)+2)

    def numeric(self):
        return self.numeric_value

    def __repr__(self):
        return self.value

    
class Suit:
    __suits = ['C', 'D', 'H', 'S']

    def __init__(self, value) -> None:
        if value not in self.__suits:
            raise ValueError
        self.value = value

    def __repr__(self):
        return self.value

class Card:
    def __init__(self, rank, suit) -> None:

        if type(rank) != Rank:
            raise TypeError
        self.rank = rank

        if type(suit) != Suit:
            raise TypeError
        self.suit = suit
    
    def __repr__(self):
        return str(self.rank)+str(self.suit)


class Deck:
    def __init__(self):

        ranks = [Rank('2'), Rank('3'), Rank('4'), Rank('5'), Rank('6'), Rank('7'), Rank('8'), Rank('9'), Rank('10'), Rank('J'), Rank('Q'), Rank('K'), Rank('A')]
        suits = [Suit('C'), Suit('D'), Suit('H'), Suit('S')]

        self.cards = [Card(x,y) for x in ranks for y in suits]
    
    def list_cards(self):
        for card in self.cards:
            print(card)
    
    def shuffle(self):
        shuffle(self.cards)
