
class Card:
     def __init__(self, suit, value, name, index):
         self.suit = suit
         self.value = value
         self.name = name
         self.index = index

def create_deck():
     deck_stack = []

     j = 0

     for x in range(4):
         for y in range(13):
             match y:
                 case 0:
                     s1 = "two of "
                 case 1:
                     s1 = "three of "
                 case 2:
                     s1 = "four of "
                 case 3:
                     s1 = "five of "
                 case 4:
                     s1 = "six of "
                 case 5:
                     s1 = "seven of "
                 case 6:
                     s1 = "eight of "
                 case 7:
                     s1 = "nine of "
                 case 8:
                     s1 = "ten of "
                 case 9:
                     s1 = "jack of "
                 case 10:
                     s1 = "queen of "
                 case 11:
                     s1 = "king of "
                 case 12:
                     s1 = "ace of "

             match x:
                 case 0:
                     s2 = "spades"
                 case 1:
                     s2 = "clubs"
                 case 2:
                     s2 = "diamonds"
                 case 3:
                     s2 = "hearts"

             j += 1

             deck_stack.append(Card(x, y, s1+s2, j))

     return deck_stack

