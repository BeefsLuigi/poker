import highcard
import draw
import check
import highcard

class Hand:
    def __init__(self, deck):
        self.draw = draw.draw(deck, 5)
        self.player_name = ''
        self.score = check.type(self.draw)
        self.highcard = highcard.get(self.draw, self.score)
        self.hand_type = Hand.get_hand_name(self.score)

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
