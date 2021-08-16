from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        print("---Computer's turn:---")
        # self.picked_gesture = (random.choice(self.gesture_list))
        self.picked_gesture = random.randrange(0,4)
        print(f'Computer has chosen {self.gesture_list[self.picked_gesture]}')

# battle = Computer()
# battle.choose_gestures()