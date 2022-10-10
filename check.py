
def type(hand):
    if (is_royal_flush(hand) > 0):
        return 10
    elif (is_straight_flush(hand) > 0):
        return 9
    elif (is_four_kind(hand) > 0):
        return 8
    elif (is_full_house(hand) > 0):
        return 7
    elif (is_flush(hand) > 0):
        return 6
    elif (is_straight(hand) > 0):
        return 5
    elif (is_three_kind(hand) > 0):
        return 4
    elif (is_two_pair(hand) > 0):
        return 3
    elif (is_two_kind(hand) > 0):
        return 2

    return 1

def is_royal_flush(hand):
    hand.sort(key=lambda x: x.value)

    if (is_flush(hand) == 0):
        return 0
    elif (is_straight(hand) == 0):
        return 0
    elif (hand[-1].value != 12):
        return 0

    return 1

def is_straight_flush(hand):
    hand.sort(key=lambda x: x.value)

    if (is_flush(hand) == 0):
        return 0
    elif (is_straight(hand) == 0):
        return 0

    return 1


#test for flush
def is_flush(hand):
    hand.sort(key=lambda x: x.value)

    for i in hand:
        if (i.suit != hand[0].suit):
            return 0
    return 1

#test for straight
def is_straight(hand):
    hand.sort(key=lambda x: x.value)
    
    i = 0
        
    while (i < 4):
        if ((hand[0].value + i) != hand[i].value):
            return 0;
        i += 1
    return 1

#test for four of a kind
def is_four_kind(hand):
    
    hand.sort(key=lambda x: x.value)
    
    count = 0
    for i in range(4):
        if (hand[0].value == hand[i].value):
            count += 1

    if (count == 4):
        return 1

    count = 0
    for x in reversed(range(1,5)):
        if (hand[1].value == hand[i].value):
            count += 1

    if (count == 4):
        return 1

    return 0

#full house is bugged and confuses three of a kind
def is_full_house(hand):
    hand.sort(key=lambda x: x.value)

    if (hand[0].value != hand[1].value):
        return 0

    if ((hand[3].value != hand[4].value)):
        return 0

    if ((hand[1].value != hand[2].value)):
        if ((hand[2].value != hand[3].value)):
            return 0
        
    return 1

#test for four of a kind
def is_three_kind(hand):
    
    hand.sort(key=lambda x: x.value)
    
    count = 0
    for i in range(3):
        if (hand[0].value == hand[i].value):
            count += 1

    if (count == 3):
        return 1

    count = 0
    for x in reversed(range(2,5)):
        if (hand[4].value == hand[i].value):
            count += 1

    if (count == 3):
        return 1

    if ((hand[1].value == hand[2].value)):
        if ((hand[2].value == hand[3].value)):
            return 1

    return 0

def is_two_pair(hand):

    hand.sort(key=lambda x: x.value)

    count = 0
    i = 0
    
    for i in range(4):
        if (hand[i].value == hand[i + 1].value):
            count += 1

    if (count == 2):
        return 1

    return 0

def is_two_kind(hand):

    hand.sort(key=lambda x: x.value)

    count = 0
    i = 0
    
    for i in range(4):
        if (hand[i].value == hand[i + 1].value):
            count += 1

    if (count == 1):
        return 1

    return 0
