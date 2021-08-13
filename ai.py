from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        print("---Computer's turn:---")
        index = 0
        for player in self.gesture_list:
            index += 1
        self.picked_gesture = (random.choice(self.gesture_list))
        print(f'Computer has chosen {self.picked_gesture}')

# battle = Computer()
# battle.choose_gestures()