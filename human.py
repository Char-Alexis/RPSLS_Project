from random import randint
import random
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        print("---Please pick your move---")
        user_validation = True
        while user_validation:
            index = 0
            for player in self.gesture_list:
                print(f'Type {index} for {player}')
                index += 1
            self.picked_gesture = int(input())
            if self.picked_gesture != range(0,5):
                user_validation = False
                return
        print(f'You have chosen {self.gesture_list[self.picked_gesture]}')