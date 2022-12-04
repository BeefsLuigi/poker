import plain_52
import draw
import check
import player
import random

def test():

    all_players = []

    deck = plain_52.create_deck()

    random.shuffle(deck)

    all_players.append(player.player('Jim'))
    all_players[-1].draw = draw.draw(deck, 2)

    all_players.append(player.player('Goku'))
    all_players[-1].draw = draw.draw(deck, 2)

    all_players.append(player.player('Tom'))
    all_players[-1].draw = draw.draw(deck, 2)

    all_players.append(player.player('Cody'))
    all_players[-1].draw = draw.draw(deck, 2)

    dealer_cards = draw.draw(deck, 5)

    hand_string = ""
    for i in dealer_cards:
        hand_string += i.name + " "

    print ("Dealer cards: " + hand_string)
    print("")

    for i in all_players:
        print (i.player_name + "'s cards: "  + i.draw[0].name + " " + i.draw[1].name)

        i.check_hand(dealer_cards)
        i.show_hand()

        print(" ")





    

test()




