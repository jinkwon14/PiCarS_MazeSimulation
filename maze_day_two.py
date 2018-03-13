import numpy as np
import copy
from sys import stdout

class PATH:
    def __init__(self, cell):
        self.path = [[cell]]

    def print_path(self):
        stdout.write('START - ')
        for cell_list in self.path:
            for cell in cell_list:
                stdout.write('{')
                stdout.write('[NO:{} OPENS:{}]'.format(cell.no, cell.openings))
                stdout.write('}')
        stdout.write(' - END \n\n')

    def append_cell(self, cell):
        # INPUT: cell is a list
        self.path.append([cell])


class CELL:
    def __init__(self, no = 3, open_dir = []):
        self.no = no
        self.openings = open_dir


class BOT:
    def __init__(self, curr_loc = 3, heading = 'N', heading_no = 0):
        self.curr_loc = curr_loc
        self.heading = heading
        self.heading_no = heading_no

    def move(self, move_to):
        # INPUT: STRING "F", "B"
        if move_to == "F":
            mult = 1
        elif  move_to == "B":
            mult = -1
        else:
            print("WRONG BOT.MOVE INPUT")

        if self.heading == "N":
            self.curr_loc += 5*mult
        elif self.heading == "E":
            self.curr_loc += 1*mult
        elif self.heading == "S":
            self.curr_loc -= 5*mult
        elif self.heading == "W":
            self.curr_loc -= 1*mult
        else:
            print("Wrong Moving INPUT")

    def turn(self, turn_dir):
        # INPUT: counter clockwise = -1, clockwise = +1
        return True

    def set_heading(self, direction):
        directions = ['N', 'E', 'S', 'W']
        self.heading_no += direction
        self.heading_no = self.heading_no%4
        self.heading = directions[self.heading_no]

    def sensor_msmt(self):
        left = left_msrmt
        right = right_msrmt
        center = center_msrmt

        msmrts = [left, right, center]
        # Take left
        return msmrts




class ENGINE:
    def __init__(self, path_tree, bot, cell):
        self.path_tree = path_tree
        self.bot = bot
        self.cell = cell

    def ask_move(self):
        move = raw_input("Please enter the number where you wanna move your bot: ")
        return move

    # def find_exit(self, ):

    def trace_back(self, path_tree, curr_pos):
        back_cell_no = []
        curr_cell_idx = len(path_tree)
        curr_cell = path_tree[curr_cell_idx]

        while len(curr_cell.openings) < 1:
            back_cell_no.append(curr_cell.no)
            curr_cell_idx -= 1
            curr_cell = path_tree[curr_cell_idx]

        back_cell_no.append(curr_cell.no)
        start_cell_no = curr_cell.no
        start_cell_open = curr_cell.openings

        return [back_cell_no, start_cell_no, start_cell_open]

    def play(self):
        found_exit = True
        # while found_exit:

        print("GAME STA RTED")
        print("INITIAL BOT POSITION: {}".format(self.bot.curr_loc))
        print("BOT HEADING: {}".format(self.bot.heading))
        self.path_tree.print_path()

        print("Turn Right, Move Forward")
        self.bot.set_heading(1)
        self.bot.move("F")
        new_cell = CELL(self.bot.curr_loc, ["N", "E"])
        self.path_tree.append_cell(new_cell)

        print("BOT POSITION: {}".format(self.bot.curr_loc))
        print("BOT HEADING: {}".format(self.bot.heading))
        self.path_tree.print_path()

        print("Turn Left, Move Forward")
        self.bot.set_heading(-1)
        self.bot.move("F")
        new_cell = CELL(self.bot.curr_loc, ["E"])
        self.path_tree.append_cell(new_cell)

        print("BOT POSITION: {}".format(self.bot.curr_loc))
        print("BOT HEADING: {}".format(self.bot.heading))
        self.path_tree.print_path()

        print("Turn Left, Move Backward")
        self.bot.set_heading(-1)
        self.bot.move("B")
        new_cell = CELL(self.bot.curr_loc, ["N"])
        self.path_tree.append_cell(new_cell)

        print("BOT POSITION: {}".format(self.bot.curr_loc))
        print("BOT HEADING: {}".format(self.bot.heading))
        self.path_tree.print_path()


        # list.remove(item)

# Psuedo-code:
# START
# BOT:
#     current_pos, current_heading
# bot.take_measurement()
# CELL:
#     cell_pos, cell_openings
# if len(openings) == 1:
#     move_to_dir = direction(N, W, E, S)
#     Delete cell_openings.the_one
#
# elif len(openings) > 1:
#     move_to_dir = CHOOSING METHOD
#     Delete cell_openings.the_one_took
#
# elif len(openings) == 0:
#     trace_back.




# Test
bot = BOT()
cell = CELL()
path = PATH(cell)

my_game = ENGINE(path, bot, cell)
my_game.play()
