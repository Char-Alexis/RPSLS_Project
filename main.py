from ai import Computer
from player import Player
from human import Human

class Game:
    def __init__(self):
        # HAS A
        self.player_one = Human()
        self.player_two = None
    
    # CAN DO
    def display_game(self):
        # Setup Phase
        # Welcome
        print("---------Welcome to Rock Paper Scissors Lizard Spock!---------")
        # Display rule, what beats what?
        print("------Best 2 out of 3 wins------")
        print("----Here is how you will win:----")
        print("----Rock crushes Scissors----")
        print("----Scissors cuts Paper----")
        print("----Paper covers Rock----")
        print("----Rock crushes Lizard----")
        print("----Lizard poisons Spock----")
        print("----Spock smashes Scissors----")
        print("----Scissors decapitates Lizard----")
        print("----Lizard eats Paper----")
        print("----Paper disproves Spock----")
        print("----pock vaporizes Rock----")


    def play_game(self, first_player, second_player):
        # Determine Game Type - Single Player or Multi?
        print("Play against another player or computer?")
        # Create players based on game type
        first_player = Human()
        second_player = input("Enter '0' for single player or '1' for Multiplayer")
        switch ={
            '0' == Human(),
            '1' == Computer(),
        }

        pass
        # Game Rounds - Repeat until one player has 2 points
        # Player one chooses a gesture 
        # -Prompt user to enter gesture
        # -Save choice somewhere
        # Player Two chooses a gesture
        # Compare gestures 
        # -Winner gets a point
        # -No points if tie round
        # Display winner of round 

        # End game 
        # Display winner of Game 
        pass

    def determine_game_type(self):
        #set self.player_two to Human or AI
        pass

fight = Game()
fight.display_game()
fight.play_game()