import random

class Board:

    def __init__(self):
        self.board = [[" 1"," 2"," 3"," 4"],
                   [" 5"," 6"," 7"," 8"],
                   [" 9","10","11","12"],
                   ["13","14","15","*"]]
        self.goal = []
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        self.empty = [3, 3]

    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string
