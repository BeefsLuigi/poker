import plain_52
import draw
import random
import check
import highcard
import hand

deck = plain_52.create_deck()

random.shuffle(deck)

hand1 = hand.Hand(deck)

for i in hand1.draw:
    print(i.name)

print ('score: ' + str(hand1.score))
print ('hand type: ' + hand1.hand_type)
print ('highcard: ' + hand1.highcard.name)
