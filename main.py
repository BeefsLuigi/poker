import plain_52
import draw
import random
import check
import highcard
import hand
import scoring


def test():

    deck = plain_52.create_deck()
    random.shuffle(deck)

    names = ['Jeanee', 'Bob', 'Allen', 'Sam', 'Bryan']

    players = []

    for i in names:
        players.append(hand.player(deck, i))


    winner = scoring.judge(players)

    for i in players:
        i.show_hand()

    print('the winner is ' + winner.player_name + ' with a ' + winner.hand_type)



test()



