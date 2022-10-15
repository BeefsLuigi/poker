import plain_52
import draw
import random
import check
import highcard

deck = plain_52.create_deck()

random.shuffle(deck)

hand1 = draw.draw(deck, 5)
hand2 = draw.draw(deck, 5)

score1 = check.type(hand1)
score2 = check.type(hand2)

print ('player 1 hand')
for i in hand1:
    print(i.name)

print ('')

print ('player 2 hand')
for i in hand2:
    print(i.name)

print ('')

if (score1 > score2):
    print ("player 1 wins")
elif(score1 < score2):
    print ("player 2 wins")
else:
    print('tie')


