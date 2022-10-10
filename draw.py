


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

    hand = []

    while (len(hand) == 0):
        if (deck[0].value == 12):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    while (len(hand) < 5):
        if (deck[0].value ==  hand[-1].value - 1) and (deck[0].suit == hand[0].suit):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
    
    return hand

# draw straight flush
def straight_flush(deck):

    hand = []

    while (len(hand) == 0):
        if (deck[0].value < 12) and (deck[0].value > 3):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    while (len(hand) < 5):
        if (deck[0].value ==  hand[-1].value - 1) and (deck[0].suit == hand[0].suit):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
    
    return hand


#draw only same suit for testing
def flush(deck):
    sample = deck[0].suit

    hand = []

    # test for flush and add to hand
    while (len(hand) < 5):
        if (deck[0].suit == sample):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
            
    return hand

#draw four of a kind
def four_kind(deck):
    sample = deck[0].value

    hand = []

    # test for same and add to hand
    while (len(hand) < 4):
        if (deck[0].value == sample):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    #draw a random card to finish hand
    hand.append(deck[0])
    deck.pop(0)
            
    return hand

#draw full house
def full_house(deck):
    sample = deck[0].value

    hand3 = []
    hand2 = []

    # test for same and add to hand
    while (len(hand3) < 3):
        if (deck[0].value == sample):
            hand3.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    sample = deck[0].value
    
    while (len(hand2) < 1):
        if (sample != hand3[0].value):
            hand2.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
    
    while (len(hand2) < 2):
        if (deck[0].value == hand2[0].value) and (sample != hand3[0].value):
            hand2.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    return hand3 + hand2

#draw three of a kind
def three_kind(deck):
    sample = deck[0].value

    hand = []

    # test for same and add to hand
    while (len(hand) < 3):
        if (deck[0].value == sample):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    #draw a random cards to finish hand
    while (len(hand) < 4):
        if (deck[0].value != hand[0].value):
            hand.append(deck[0])
            deck.pop(0)
            break
        else:
            deck.append(deck[0])
            deck.pop(0)

        
    while (len(hand) < 5):
        if (deck[0].value != hand[3].value) and (deck[0].value != hand[0].value):
            hand.append(deck[0])
            deck.pop(0)
            break
        else:
            deck.append(deck[0])
            deck.pop(0)

    return hand

#draw two pair
def two_pair(deck):
    sample1 = deck[0].value

    handhalf1 = []
    handhalf2 = []
    handfull = []


    # test for same and add to hand
    while (len(handhalf1) < 2):
        if (deck[0].value == sample1):
            handhalf1.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
    
    while (len(handhalf2) < 1):
        if (deck[0].value != sample1):
            handhalf2.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    sample2 = handhalf2[0].value

    while (len(handhalf2) < 2):
        if (deck[0].value == sample2) and (deck[0].value != sample1):
            handhalf2.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    handfull = handhalf1 + handhalf2

    while (len(handfull) < 5):
        if (deck[0].value != sample1) and (deck[0].value != sample2):
            handfull.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
            
    return handfull

def two_kind(deck):
    sample = deck[0].value

    hand = []

    # test for same and add to hand
    while (len(hand) < 2):
        if (deck[0].value == sample):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    #draw a random cards to finish hand
    while (len(hand) < 3):
        if (deck[0].value != hand[0].value):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    while (len(hand) < 4):
        if (deck[0].value != hand[0].value) and (deck[0].value != hand[2].value):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

        
    while (len(hand) < 5):
        if (deck[0].value != hand[0].value) and (deck[0].value != hand[2].value) and (deck[0].value != hand[3].value):
            hand.append(deck[0])
            deck.pop(0)
            break
        else:
            deck.append(deck[0])
            deck.pop(0)

    return hand



#draw only cards in order for testing
def straight(deck):
    hand = []
    hand.append(deck[0])

    while (len(hand) < 2):
        if (deck[0].value == hand[0].value + 1) or (deck[0].value == hand[0].value - 1):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)
    
    if (hand[0].value > hand[1].value):
        hand.append(hand[0])
        hand.pop(0)
    
    while (len(hand) < 5):
        if (deck[0].value == hand[0].value - 1):
            hand.insert(0, deck[0])
            deck.pop(0)
        elif (deck[0].value == hand[-1].value + 1):
            hand.append(deck[0])
            deck.pop(0)
        else:
            deck.append(deck[0])
            deck.pop(0)

    return hand


