
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
                     s1 = "2"
                 case 1:
                     s1 = "3"
                 case 2:
                     s1 = "4"
                 case 3:
                     s1 = "5"
                 case 4:
                     s1 = "6"
                 case 5:
                     s1 = "7"
                 case 6:
                     s1 = "8"
                 case 7:
                     s1 = "9"
                 case 8:
                     s1 = "T"
                 case 9:
                     s1 = "J"
                 case 10:
                     s1 = "Q"
                 case 11:
                     s1 = "K"
                 case 12:
                     s1 = "A"

             match x:
                 case 0:
                     s2 = "\u2664"
                 case 1:
                     s2 = "\u2667"
                 case 2:
                     s2 = "\u2662"
                 case 3:
                     s2 = "\u2661"

             j += 1

             deck_stack.append(Card(x, y, s2 + s1, j))

     return deck_stack

