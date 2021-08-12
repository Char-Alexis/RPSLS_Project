from player import Player


class Game:
    def __init__(self):
        # HAS A
        self.player_one = Human()
        self.player_two = None
    
    # CAN DO
    def run_game(self):
        # Setup Phase
        # Welcome
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        # Display rule, what beats what?
        print("Rules of game:... Best 2 out of 3 wins")
        # Determine Game Type - Single Player or Multi?
        print("Play against another player or computer?")
        # Create players based on game type



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

    print("Play against another player or computer?")

    print("Do you want to start game? Yes or No?")

    print("Pick your choice: 1, 2, 3, 4, 5")