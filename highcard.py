import copy

def get(hand, hand_type):

    hand.sort(key=lambda x: x.value)
    
    match hand_type:
        case 10:
            return royal_flush(hand)
        case 9:
            return straight_flush(hand)
        case 8:
            return four_kind(hand)
        case 7:
            return full_house(hand)
        case 6:
            return flush(hand)
        case 5:
            return straight(hand)
        case 4:
            return three_kind(hand)
        case 3:
            return two_pair(hand)
        case 2:
            return two_kind(hand)
        case 1:
            return just_highcard(hand)


def royal_flush(hand):
    sample = hand[0]

    for i in hand:
        if (sample.value < i.value):
            sample = i
    
    return sample

def straight_flush(hand):
    sample = hand[0]

    for i in hand:
        if (sample.value < i.value):
            sample = i
    
    return sample

def four_kind(hand):
    hand_copy = hand

    if (hand[0] != hand[1]):
        hand_copy.pop(0)
    else:
        hand_copy.pop(4)
    
    sample = hand_copy[0]

    for i in hand_copy:
        if sample.suit < i.suit:
            sample = i
    
    return sample



def full_house(hand):
    hand_copy = copy.copy(hand)

    if (hand[1].value != hand[2].value):
        hand_copy.pop(0)
        hand_copy.pop(0)
    else:
        hand_copy.pop(4)
        hand_copy.pop(4)
    
    sample = hand_copy[0]

    for i in hand_copy:
        if sample.suit < i.suit:
            sample = i
    
    return sample

def flush(hand):
    sample = hand[0]

    for i in hand:
        if (sample.value < i.value):
            sample = i
    
    return sample

def straight(hand):
    sample = hand[0]

    for i in hand:
        if (sample.value < i.value):
            sample = i
    
    return sample

def three_kind(hand):

    sample = hand[4].value

    for i in hand:
        if (sample != i.value):
            sample = i.value
        else:
            break
    
    hand_copy = [x for x in hand if x.value == sample]

    highcard = copy.copy(hand_copy[0])

    for i in hand_copy:
        if (highcard.suit < i.suit):
            highcard = copy.copy(i)

    return highcard

def two_pair(hand):
    hand_copy = copy.copy(hand)

    pair1 = []
    pair2 = []

    sample = copy.copy(hand_copy[0])

    while (hand_copy[0].value != hand_copy[1].value):
        hand_copy.append(hand_copy[0])
        hand_copy.pop(0)

    pair1.append(hand_copy[0])
    hand_copy.pop(0)
    pair1.append(hand_copy[0])
    hand_copy.pop(0)

    while (hand_copy[0].value != hand_copy[1].value):
        hand_copy.append(hand_copy[0])
        hand_copy.pop(0)

    pair2.append(hand_copy[0])
    hand_copy.pop(0)
    pair2.append(hand_copy[0])
    hand_copy.pop(0)

    
    pair1.sort(key=lambda x: x.suit)
    pair2.sort(key=lambda x: x.suit)

    if (pair1[1].value > pair1[1].value):
        return pair1[1]
    else:
        return pair2[1]


def two_kind(hand):

    while(hand[0].value != hand[1].value):
        hand.append(hand[0])
        hand.pop(0)

    if(hand[0].suit > hand[1].suit):
        return hand[0]
    else:
        return hand[1]


    pass

def just_highcard(hand):

    sample = hand[0]

    for i in hand:
        if (sample.value < i.value):
            sample = i
    
    return sample




