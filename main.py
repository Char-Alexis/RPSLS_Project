from ai import Computer
from human import Human
from player import Player

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


    def play_game(self):
        # Determine Game Type - Single Player or Multi?
        print("Play against another player or computer?")
        self.second_player = int(input("Enter '0' for single player or '1' for Multiplayer "))
        if self.second_player == 0:
            self.second_player = Computer()
        elif self.second_player == 1:
            self.second_player = Human()
        # Create players based on game type
        self.first_player = Human()
        # self.second_player = Human()
        self.first_player.choose_gestures()
        self.second_player.choose_gestures()

        
    def determine_winner(self):
        # self.first_player = 
        # if spock or paper:
        #     beats rock
        # self.winning_combinations = Human(Player)
        self.play_game()
        if self.first_player == self.second_player:
            print ("test")

        # if scissors or lizard:
        #     beats paper
        # if rock or spock:
        #      beats scissors
        # if scissors or rock:
        #     beat lizard
        # if scissors or paper:
        #     beat spock

        
        


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
        

    def determine_game_type(self):
        #set self.player_two to Human or AI
        pass

fight = Game()
fight.display_game()
fight.play_game()
fight.determine_winner()