import plain_52
import draw
import check
import player


deck = plain_52.create_deck()

hand = draw.type(deck, 'two of a kind')

test_player = player.player('Jim')

hand.sort(key=lambda x: x.value)

hand_string = ""

for i in hand:
    hand_string += i.name + ' '

print(hand_string)

print('')

test_player.check_hand(hand)

#flush_hand = test_player.get_flush(hand)
#straight_hand = test_player.get_straight(hand)
#match_hand = test_player.get_match(hand)





