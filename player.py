#Properties
# self.chosen_gesture = ""
# self.score = 0
# self.name = ""
# self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

<<<<<<< HEAD
class Player(Parent):
    def __init__ (self, name):
        self.name = name
=======
#Methods
#choose_gesture() - Overrides it!
>>>>>>> 57974f314c5bde7d0f57cfb8e38ae3ca93fc1ab1

class Player:
    def __init__ (self):
        self.picked_gesture = ""
        self.score = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    def choose_gestures(self):
        pass