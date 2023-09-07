import card_game as cg

player1 = cg.Player('player1')
player2 = cg.Player('player2')

myTable = cg.Table()
myTable.add_player(player1, 2.00)
myTable.add_player(player2, 2.00)
myDealer = cg.Dealer(myTable)
myDealer.shuffle_deck()

myDealer.deal_cards(2)

for player in [player1,player2]:
    print(player.name, player.hand, player.stack)