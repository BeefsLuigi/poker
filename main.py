import plain_52
import draw
import random
import check

deck = plain_52.create_deck()

random.shuffle(deck)

hand1 = draw.type(deck, 'two pair')

for i in hand1:
    print(i.name)


print (check.type(hand1))