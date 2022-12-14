import copy


def type(hand):
    hand.sort(key=lambda x: x.value)

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

    if (is_flush(hand) == 0):
        return 0
    elif (is_straight(hand) == 0):
        return 0
    elif (hand[-1].value != 12):
        return 0

    return 1

def is_straight_flush(hand):
    
    if (is_flush(hand) == 0):
        return 0
    elif (is_straight(hand) == 0):
        return 0

    return 1


#test for flush
def is_flush(hand):
    
    for i in range (4):
        if (grab_suit(hand, i) != None):
            return 1

    return 0

def grab_suit(hand, test_suit):
    cards = []

    for i in hand:
        if (i.suit == test_suit):
            temp_card = copy

            cards.append(i)

    if (len(cards) >= 5):
        return cards
    else:
        return None



#test for straight
def is_straight(hand):
    
    i = 0
        
    while (i < 4):
        if ((hand[0].value + i) != hand[i].value):
            return 0
        i += 1
    return 1

#test for four of a kind
def is_four_kind(hand):

    count = 0
    for i in hand:
        if (hand[0].value == i.value):
            count += 1

    if (count == 4):
        return 1

    count = 0
    for i in reversed(hand):
        if (hand[-1].value == i.value):
            count += 1

    if (count == 4):
        return 1

    return 0



def is_full_house(hand):

    count = 0
    for i in hand:
        if (hand[0].value == i.value):
            count += 1

    if (count != 3):

        count = 0
        for i in reversed(hand):
            if (hand[-1].value == i.value):
                count += 1

        if (count != 3):
            return 0

    if (hand[0].value != hand[1].value) or (hand[-1].value != hand[-2].value):
        return 0
    
    
    return 1


#test for three of a kind
def is_three_kind(hand):
    sample = hand[0].value
    count = 1

    for i in range(1,5):
        if (sample == hand[i].value):
            count += 1
        else:
            sample = hand[i].value
            if(count != 3):
                count = 1
    if (count != 3):
        return 0
        

    return 1



def is_two_pair(hand):
    pair_count = 0
    sample = hand[0].value

    for i in range(1,5):
        if (sample == hand[i].value):
            pair_count += 1
        else:
            sample = hand[i].value

    if (pair_count == 2):
        return 1

    return 0




def is_two_kind(hand):

    count = 0
    i = 0
    
    for i in range(4):
        if (hand[i].value == hand[i + 1].value):
            count += 1

    if (count == 1):
        return 1

    return 0
