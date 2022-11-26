
import plain_52
import draw
import random
import check
import highcard
import player
import scoring




class Core():

    def __ini__(self):
        self.state = 0
        self.player_pool = []
        self.bet_limit = 0
        self.deck = plain_52.create_deck()
        self.flop = []

    def game_loop(self):
        
        random.shuffle(self.deck)

        self.test_players()

        #player actions

        #first flop

        #player actions

        #second flop

        #river and final showdown

        #player actions

        #winnings dealt

        #game ends, maybe sends players back just in case for new game
        pass


    def poll_actions(self):

        bets_equal = False
        can_check = True


        while(bets_equal == False):
            break
        
        # what options available to the player should be dynamic
        # in that they should only be able to play actions that are
        # possible. EX: a player should not be able to check if someone
        # before them bets. it should look like this to them
 
        # 1. bet
        # 2. fold

        # but on the first flop with no one betting yet...

        # 1. bet
        # 2. check
        # 3. fold




        pass

    def player_actions(self, action):

        match action:
            case 1: 
                self.bet()
            case 2:
                self.fold()
            case 3:
                self.check()

        pass


    def test_players(self):
        names = ['Jeanee', 'Bob', 'Allen', 'Sam', 'Bryan']

        for i in names:
            self.player_pool.append(player.player(self.deck, i))


    def bet(self, player):
        pass

    def check(self, player):
        pass

    def fold(self, player):
        pass
