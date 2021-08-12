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

        print (self.gesture_list)       

battle = Human()
battle.choose_gestures()