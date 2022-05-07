from game_window import Window

#--------USED TO INITIALIZE THE WINDOW IN A CLASS AND TO PASS ARGUMENTS------
class Game:
    def __init__(self,marbles=0,score=0):
        # create window object (actual game)
        self.window = Window(marbles,score)
