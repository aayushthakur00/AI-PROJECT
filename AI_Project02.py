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

    def convert_to_tuple(self, ar):
        result = []
        for i in ar:
            result.append(tuple(i))
        return tuple(result)

    def convert_to_list(self, tup):
        result = []
        for i in tup:
            result.append(list(i))
        return result

    def match(self, copy):
        a = Board()
        a.board = copy
        for row in range(0, 4):
            for col in range(0, 4):
                if a.board[row][col] == '*':
                    a.empty = [row, col]
        result = []
        for i in a.board:
            result.append(list(i))
        a.board = result
        return a

