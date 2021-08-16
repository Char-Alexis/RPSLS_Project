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
        self.final_screen()

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
        print("----Spock vaporizes Rock----")


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
        
    def determine_winner(self):
        
        while self.first_player.score < 2 and self.second_player.score < 2:
            print("Player one score is " + str(self.first_player.score))
            print("Player Two score is " + str(self.second_player.score))
            self.first_player.choose_gestures()
            self.second_player.choose_gestures()
# TIE
            if self.first_player.picked_gesture == self.second_player.picked_gesture:
                print("Its a tie!")

# ROCK

            elif self.first_player.picked_gesture == 0:
                if self.second_player.picked_gesture == 1:
                    print("Second player wins, Paper covers Rock")
                    self.second_player.score += 1
                    

                elif self.second_player.picked_gesture == 2:
                    print("First player wins, Rock crushes Scissors ")
                    self.first_player.score += 1
                    

                elif self.second_player.picked_gesture == 3:
                    print("First player wins, Rock crushes Lizard")
                    self.first_player.score += 1
                    

                elif self.second_player.picked_gesture == 4:
                    print ("Second player wins, Spock vaporizes Rock")
                    self.second_player.score += 1                   
# PAPER

            elif self.first_player.picked_gesture == 1:
                if self.second_player.picked_gesture == 0:
                    print ("First player wins, Paper covers Rock ")
                    self.first_player.score +=1

                elif self.second_player.picked_gesture == 2:
                    print("Second player wins, Scissors cuts Paper")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 3:
                    print ("Second player wins, Lizard eats Paper")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("First player wins, Paper disproves Spock")
                    self.first_player.score += 1


# SCISSORS
            elif self.first_player.picked_gesture == 2:
                if self.second_player.picked_gesture == 0:
                    print ('Second player wins, Rock crushes Scissors')
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print ("First player wins, Scissors cuts Paper ")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 3:
                    print ("First player wins, Scissors decapitates Lizards")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("Second player wins, Spock smashes Scissors")
                    self.second_player.score +=1


# LIZARD

            elif self.first_player.picked_gesture == 3:
                if self.second_player.picked_gesture == 0:
                    print ("Second player wins, Rock crushes Lizard")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print ("First player wins, Lizard eats Paper")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 2:
                    print ("Second player wins, Scissors decapitates Lizard")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 4:
                    print ("First player wins, Lizard poisons Spock")
                    self.first_player.score += 1

        
# SPOCK

            elif self.first_player.picked_gesture == 4:
                if self.second_player.picked_gesture == 0:
                    print("First player wins, Spock vaporizes Rock")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture == 1:
                    print("Second player wins, Paper disproves Spock")
                    self.second_player.score += 1

                elif self.second_player.picked_gesture == 2:
                    print ("First player wins, Spock smashes Scissors")
                    self.first_player.score += 1

                elif self.second_player.picked_gesture ==3:
                    print ("Second player wins, Lizard poisons Spock")
                    self.second_player.picked_gesture +=1
            
            else:
                print("Please try again")
            
    
    def final_screen(self):
        if self.first_player.score == 2:
            print(f'Congratulations Player One for winning the game!')
        elif self.second_player.score == 2:
            print(f'Congratulations Player Two for winning the game!')

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