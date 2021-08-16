from ai import Computer
from human import Human
from player import Player

class Game:
    def __init__(self):
        # HAS A
        self.first_player = Human()
        self.second_player = Computer()
    
        # CAN DO
    def run(self):
        self.display_game()
        self.play_game()
        self.determine_winner()

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
        
    def determine_winner(self):
        
        while self.first_player.score < 2 or self.second_player.score <2:

            self.first_player.choose_gestures()
            self.second_player.choose_gestures()

            # self.first_player = 
            # self.winning_combinations = Human(Player)
            # self.play_game()

# TIE
            if self.first_player.picked_gesture == self.second_player.picked_gesture:
                print("Its a tie!")

# ROCK

            elif self.first_player.picked_gesture == 0:
                if self.second_player.picked_gesture == 1:
                    print("Second player wins, paper covers rock")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 2:
                    print("first player wins, rock beats scissors ")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 3:
                    print("first player wins, rock crushes lizard")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("second player wins, spock crushes rock")
                    self.second_player.score += 1


# PAPER

            elif self.first_player.picked_gesture == 1:
                if self.second_player.picked_gesture == 0:
                    print ("first player wins")
                    self.first_player.score +=1

                elif self.second_player.picked_gesture == 2:
                    print("second player wins")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 3:
                    print ("second player wins, lizard crushes paper")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("first player wins, paper crushes spock")
                    self.first_player.score += 1


# SCISSORS
            elif self.first_player.picked_gesture == 2:
                if self.second_player.picked_gesture == 0:
                    print ('second player wins')
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print ("first player wins")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 3:
                    print ("first player wins, scissors crushes lizards")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("second player wins, scissors crushes spock")
                    self.second_player.score +=1


# LIZARD

            elif self.first_player.picked_gesture == 3:
                if self.second_player.picked_gesture == 0:
                    print ("second player wins, rock crushes lizard")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print ("first player wins, lizard crushes paper")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 2:
                    print ("second player wins, scissors crushes lizard")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("first player wins, lizard crushes spock")
                    self.first_player.score += 1

        
# SPOCK

            elif self.first_player.picked_gesture == 4:
                if self.second_player.picked_gesture == 0:
                    print("first player wins, spock crushes rock")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print("second player wins, paper crushes spock")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 2:
                    print ("first player wins, spock crushes scissors")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture ==3:
                    print ("second player wins, lizard crushes spock")
                    self.second_player.picked_gesture +=1

        
        


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





# fight.play_game()
# fight.determine_winner()
# print(fight.first_player.score)
# print(fight.second_player.score)
# fight.best_of
