import plain_52
import draw
import random
import check
import highcard
import hand
import scoring


deck = plain_52.create_deck()
random.shuffle(deck)

names = ['Steve', 'Amber', 'Jim', 'Mike', 'Goku']

players = []

for i in names:
    players.append(hand.player(deck, i))


winner = scoring.judge(players)

for i in players:
    i.show_hand()

print('the winner is ' + winner.player_name + ' with a ' + winner.hand_type)

#print ('score: ' + str(hand1.score))
#print ('hand type: ' + hand1.hand_type)
#print ('highcard: ' + hand1.highcard.name)
