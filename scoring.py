import copy

def judge(players):
    
    players.sort(key=lambda x: x.score)

    tied= []

    sample = copy.copy(players[-1])

    for i in players:

        if (sample.score == i.score):
            tied.append(copy.copy(i))

    if(len(tied) == 1):
        return sample

    tied.sort(key=lambda x: x.highcard.value)

    sample = copy.copy(tied[-1])

    tied_highcard = []

    for i in tied:

        if (sample.highcard.value == i.highcard.value):
            tied_highcard.append(copy.copy(i))

    if(len(tied_highcard) == 1):
        return sample

    tied_highcard.sort(key=lambda x: x.highcard.suit)

    return tied_highcard[-1]

