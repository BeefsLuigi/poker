from unicodedata import name
import highcard
import draw
import check
import highcard
import copy

class player:
    def __init__(self, player_name):
        self.draw = []
        self.hand = []
        self.player_name = player_name
        self.state = 1
        self.bet = 0
        self.winnings = 100
        self.score = 0
        self.highcard = None
        self.hand_type = 0

    # checks the player hand, trims it, and stores it for later
    def check_hand(self, deal):
        self.s_f_flag = 0

        self.hand.sort(key=lambda x: x.value)

        hand_plus_dealer = self.hand + deal

        hand_flush = copy.copy(self.get_flush(hand_plus_dealer))
        hand_straight = copy.copy(self.get_straight(hand_plus_dealer))
        hand_match = copy.copy(self.get_match(hand_plus_dealer))

        # check for royal flush
        if (self.is_royal_flush(hand_flush, hand_straight) == 1):
            
            while(len(hand_flush) > 5):
                hand_flush.pop(0)

            for i in hand_flush:
                print (i.name)

            self.hand = hand_flush

            print('found royal flush')
        # check for straight flush
        elif (self.is_straight_flush(hand_flush, hand_straight) == 1):
            hand_flush = self.get_straight(hand_flush)

            while(len(hand_flush) > 5):
                hand_flush.pop(0)

            for i in hand_flush:
                print (i.name)

            self.hand = hand_flush

            print('found straight flush')
        # check for four of a kind
        elif(self.is_four_kind(hand_match) == 1):
            for i in hand_match:
                if (len(i) == 4):
                    self.hand = i

            for k in self.hand:
                print (k.name)

            print('found four of a kind')
        # check for full house
        elif(self.is_full_house(hand_match) == 1):
            match_3 = None
            match_2 = []

            for i in hand_match:
                if (len(i) == 3):
                    match_3 = i

            for i in hand_match:
                if (len(i) == 2):
                    match_2.append(i)
            
            self.hand = match_3 + match_2[-1]

            for k in self.hand:
                print (k.name)

            print('found full house')
        # check for flush
        elif(hand_flush != None):
            while(len(hand_flush) > 5):
                hand_flush.pop(0)
            
            self.hand = hand_flush

            for k in self.hand:
                print (k.name)

            print ('found flush')
        # check for straight
        elif(hand_straight != None):
            while(len(hand_straight) > 5):
                hand_straight.pop(0)
            
            self.hand = hand_straight

            for k in self.hand:
                print (k.name)

            print ('found straight')
        # check for three of a kind
        elif(self.is_three_kind(hand_match) == 1):
            match_3 = []

            for i in hand_match:
                if (len(i) == 3):
                    match_3.append(i)

            self.hand = match_3[-1]

            for k in self.hand:
                print (k.name)

            print ('found three of a kind')
        # check for two pair
        elif(self.is_two_pair(hand_match)):
            match_2 = []

            for i in hand_match:
                if (len(i) == 2):
                    match_2.append(i)

            self.hand = match_2[-1] + match_2[-2]

            for k in self.hand:
                print(k.name)

            print ('found two pair')
        # check for two of a kind
        elif(self.is_two_kind(hand_match)):
            match_2 = []

            for i in hand_match:
                if (len(i) == 2):
                    match_2.append(i)

            self.hand = match_2[-1]

            for k in self.hand:
                print(k.name)

            print ('found two of a kind')
        # all that's left is the high card
        else:
            print('only high card')

        pass


    def show_hand(self):

        print ('player name: ' + self.player_name)
        print ('hand type: ' + self.hand_type)
        print ('high card: ' + self.highcard.name)

        for i in self.draw:
            print (i.name)

        print('')

    def get_hand_name(score):

        match score:
            case 10:
                return 'royal flush'
            case 9:
                return 'straight flush'
            case 8:
                return 'four of a kind'
            case 7:
                return 'full house'
            case 6:
                return 'flush'
            case 5:
                return 'straight'
            case 4:
                return 'three of a kind'
            case 3:
                return 'two pair'
            case 2:
                return 'two of a kind'
            case 1:
                return 'high card'


    #functions for testing hand type

    # It takes the combined player and dealer hand
    # and makes it return either flushes, straights, or
    # matches. If any of these functions fail to make
    # a usable object, it will return nothing. These 
    # functions should cut down the repetition when checking the
    # 10 different types of poker hands that a player can use
    def get_flush(self, hand):
        
        cards = []

        for i in range (4):

            for k in hand:
                if (k.suit == i):
                    cards.append(k)

            if (len(cards) >= 5):
                return cards
            else:
                cards.clear()

        return None
    
    def get_match(self, hand):
        all_matches = []

        index_pos = 0

        all_matches.append(list())
        all_matches[index_pos].append(hand[0])

        for i in range(1, len(hand)):
            if (all_matches[index_pos][-1].value != hand[i].value) and (len(all_matches[index_pos]) == 1):
                all_matches[index_pos].pop(-1)
                all_matches[index_pos].append(hand[i])
            elif (all_matches[index_pos][-1].value != hand[i].value) and (len(all_matches[index_pos]) > 1):
                index_pos += 1
                all_matches.append(list())
                all_matches[index_pos].append(hand[i])
            elif(all_matches[index_pos][-1].value == hand[i].value):
                all_matches[index_pos].append(hand[i])


        # If the length of the first element is 1, that
        # should mean that there weren't any matches found
        if(len(all_matches[0]) == 1):
            return None
        else:
            return all_matches

    def get_straight(self, hand):
        cards = []

        cards.append(hand[0])

        for i in range(1, len(hand)):
            
            if(cards[-1].value == hand[i].value):
                if(cards[-1].suit < hand[i].suit):
                    cards.pop(-1)
                    cards.append(hand[i])
            elif(cards[-1].value + 1 == hand[i].value):
                cards.append(hand[i])
            elif (cards[-1].value + 1 < hand[i].value) and (i < 3):
                cards.pop(-1)
                cards.append(hand[i])

        if (len(cards) >= 5):
            return cards

        return None

#functions for checking hand type

    def is_royal_flush(self, flush, straight):

        # early out
        if (flush == None) or (straight == None):
            return 0
        
        royal_flush = self.get_straight(flush)

        if (royal_flush == None):
            return 0
        elif ( royal_flush[-1].value != 12):
            return 0
        
        return 1

    def is_straight_flush(self, flush, straight):

            # early out
        if (flush == None) or (straight == None):
            return 0
        
        straight_flush = self.get_straight(flush)

        if (straight_flush == None):
            return 0

        return 1

    def is_four_kind(self, match_list):
        if (match_list == None):
            return 0

        for i in match_list:
            if (len(i) ==  4):
                return 1
        
        return 0

    def is_full_house(self, match_list):
        if (match_list == None):
            return 0

        threes_list = []
        twos_list = []

        for i in match_list:
            if (len(i) == 3):
                threes_list.append(i)
            if (len(i) == 2):
                twos_list.append(i)

        if (len(threes_list) == 0):
            return 0
        elif (len(twos_list) == 0):
            return 0
        else:
            return 1

    def is_three_kind(self, match_list):
        if(match_list == None):
            return 0

        threes_list = []
        
        for i in match_list:
            if (len(i) == 3):
                threes_list.append(i)

        if (len(threes_list) == 0):
            return 0
        
        return 1

    def is_two_pair(self, match_list):
        if(match_list == None):
            return 0

        twos_list = []
        
        for i in match_list:
            if (len(i) == 2):
                twos_list.append(i)

        if (len(twos_list) < 2):
            return 0
        
        return 1

    def is_two_kind(self, match_list):
        if(match_list == None):
            return 0

        twos_list = []
        
        for i in match_list:
            if (len(i) == 2):
                twos_list.append(i)

        if (len(twos_list) != 1):
            return 0
        
        return 1

#code for trimming hands down to five cards
"""
if (len(cards) == 5):
            return cards
        elif (len(cards) > 5):
            cards.sort(key=lambda x: x.value)
            while(len(cards) > 5):
                cards.pop(0)
            return cards
        else:
            cards.clear

        return None

"""