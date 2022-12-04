
import random

def draw(deck, amount):
    hand = []
    
    # standard draw
    for i in range(amount):
        hand.append(deck[0])
        deck.pop(0)
    return hand


#draw 
def type(deck, hand_type):
    hand = []

    match hand_type:
        case 'royal flush':
            hand = royal_flush(deck)
        case 'straight flush':
            hand = straight_flush(deck)
        case 'flush':
            hand = flush(deck)
        case 'straight':
            hand = straight(deck)
        case 'four of a kind':
            hand = four_kind(deck)
        case 'full house':
            hand = full_house(deck)
        case 'three of a kind':
            hand = three_kind(deck)
        case 'two pair':
            hand = two_pair(deck)
        case 'two of a kind':
            hand = two_kind(deck)

   
    return hand

# draw royal flush for testing
def royal_flush(deck):
   
    hand = sequence(deck, random.randrange(0, 4), 12, 1)

    fill_hand(deck, hand, 7)

    return hand

# draw straight flush
def straight_flush(deck):

    hand = sequence(deck, random.randrange(0, 4), random.randrange(4, 12), 1)

    fill_hand(deck, hand, 7)

    return hand

#draw only same suit for testing
def flush(deck):
    random.shuffle(deck)

    sample_suit = deck[0].suit

    hand = []

    # test for matchin suit and add to hand
    while (len(hand) < 5):
        if (deck[0].suit == sample_suit):
            hand.append(deck[0])
            deck.pop(0)     
        else:
            deck.append(deck[0])
            deck.pop(0)
     
    fill_hand(deck, hand, 7)

    return hand

#draw four of a kind
def four_kind(deck):
    random.shuffle(deck)

    sample = deck[0].value

    hand = match_value(deck, sample, 4)

    fill_hand(deck, hand, 7)

    return hand

#draw full house
def full_house(deck):
    sample1 = random.randrange(0, 13)
    sample2 = random.randrange(0, 13)

    while (sample1 == sample2):
        sample2 = random.randrange(0, 13)

    hand_part_1 = match_value(deck, sample1, 3)
    hand_part_2 = match_value(deck, sample2, 2)

    hand = hand_part_1 + hand_part_2

    fill_hand(deck, hand, 7)

    return hand

#draw three of a kind
def three_kind(deck):
    sample = random.randrange(0, 13)

    hand = match_value(deck, sample, 3)

    fill_hand(deck, hand, 7)

    return hand

#draw two pair
def two_pair(deck):
    sample1 = random.randrange(0, 13)
    sample2 = random.randrange(0, 13)

    while (sample1 == sample2):
        sample2 = random.randrange(0, 13)

    hand_part_1 = match_value(deck, sample1, 2)
    hand_part_2 = match_value(deck, sample2, 2)

    hand = hand_part_1 + hand_part_2

    fill_hand(deck, hand, 7)

    return hand

def two_kind(deck):

    random.shuffle(deck)

    sample = deck[0].value

    hand = match_value(deck, sample, 2)

    fill_hand(deck, hand, 7)

    return hand

def straight(deck):
    
    hand = sequence(deck, random.randrange(0, 4), random.randrange(4, 12), 0)

    fill_hand(deck, hand, 7)
    
    return hand

def sequence(deck, suit_target, limit, match_suit):

    hand = []

    # if a royal flush or a straight flush
    if(match_suit == 1):
        x = 2
        i = 0

        while (i < len(deck)):
            if (deck[i].suit == suit_target) and (deck[i].value == limit):
                hand.append(deck[i])
                deck.pop(i)
                break
            i += 1

        while(len(hand) < 5):
            temp_index = hand[0].index - x
            temp_card = deck[temp_index]

            hand.append(temp_card)
            deck.pop(temp_index)
            x += 1
    else: #if just a straight
        random.shuffle(deck)
        lower = 1
        upper = 1

        # find sample
        while (len(hand) == 0):
            if (deck[0].value == limit):
                hand.append(deck[0])
                deck.pop(0)
                break
            else:
                deck.append(deck[0])
                deck.pop(0)

        # find the other cards
        while(len(hand) < 5):
            if(deck[0].value == hand[0].value - lower):
                hand.append(deck[0])
                deck.pop(0)
                lower += 1
            elif(deck[0].value == hand[0].value + upper):
                hand.append(deck[0])
                deck.pop(0)
                upper += 1

            else:
                deck.append(deck[0])
                deck.pop(0)

    return hand

def match_value(deck, value, amount):

    hand = []

    while (len(hand) < amount):
        if (deck[0].value == value):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    return hand

def fill_hand(deck, hand, amount):
    random.shuffle(deck)

    while (len(hand) < amount):
        hand.append(deck[0])
        deck.pop(0)
