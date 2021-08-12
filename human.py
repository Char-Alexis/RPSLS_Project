from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        print("Please pick your move")
        index = 0
        for player in self.gesture_list:
            print(f'Type {index} for {player}')
            index += 1
        self.picked_gesture = input()
        print(self.picked_gesture)

    def pick_gesture(self):
        pass



battle = Human()
battle.choose_gestures()

