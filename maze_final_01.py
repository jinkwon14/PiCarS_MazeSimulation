# import numpy as np
import copy
from sys import stdout
import numpy as np


###############################################################################
class CELL:
    def __init__(self, cell_no = 25, open_dir = []):
        self.cell_no = cell_no
        self.openings = open_dir

###############################################################################
class PATH:
    def __init__(self, cell):
        self.path = [cell]
        self.visited_cells = ["00000", "00000", "00100"]
        self.exit_cells = [1, 2, 3, 4, 5, 6, 7,
                           8, 14, 15, 21, 22, 28]

    def add_visited(self, cell_no):
        no = cell_no
        row_idx = np.int(np.round(no/7))-2
        col_idx = (no-1)%7 -1
        row = self.visited_cells[row_idx]
        visited = list(row)
        visited[col_idx] = "1"
        self.visited_cells[row_idx] = "".join(visited)

        print("VISITED CELLS: {}".format(self.visited_cells))

    def check_bingo_and_update_exit_cells(self):
        for row_no, row in enumerate(self.visited_cells):
            if "111" in row:
                bingo_starting_idx = row.find("111")

                if bingo_starting_idx == 0:
                    self.exit_cells.extend([12, 19, 26])
                elif bingo_starting_idx == 1:
                    self.exit_cells.extend([9, 16, 23, 13, 20, 13, 20, 27])
                elif bingo_starting_idx == 2:
                    self.exit_cells.extend([10, 17, 24])
                return(bingo_starting_idx)

        return False

    def mark_map_end(self, cell_no, cell_dir):
        no = cell_no
        col_idx = (no-1)%7
        row_idx = np.int(np.round(no/7))-1
        print("OPENING IS AT CELL {} DIRECTION {}".format(cell_no, cell_dir))

    def check_exit_avail(self, curr_cell, avail_opens):
        possible_exit_cells = {}

        for open_dir in avail_opens:
            if open_dir == 0:
                next_cell = curr_cell - 7
                possible_exit_cells[next_cell] = 0
            elif open_dir == 2:
                next_cell = curr_cell + 7
                possible_exit_cells[next_cell] = 2
            elif open_dir == 1:
                next_cell = curr_cell + 1
                possible_exit_cells[next_cell] = 1
            elif open_dir == 3:
                next_cell = curr_cell - 1
                possible_exit_cells[next_cell] = 3
        print("POSSIBLE MOVES: {}".format(possible_exit_cells))
        print("POSSIBLE EXITS: {}".format(self.exit_cells))

        for next_cell, direction in possible_exit_cells.iteritems():
            print(next_cell)
            if next_cell in self.exit_cells:
                print("FOUND EXIT")
                print("EXIT: {} {}".format(next_cell, direction))
                return direction
        return False


    def print_path(self):
        stdout.write('>>>  START - ')
        for cell in self.path:
            stdout.write('[CELL_NO:{} OPENS:{}] - '.format(cell.cell_no, cell.openings))
        stdout.write(' END \n')

    def append_cell(self, cell):
        self.path.append(cell)

    def most_recent_cell(self):
        cell = self.path[-1]
        return cell

    def delete_opening(self, opening):
        new_open = []
        old_open = copy.deepcopy(self.path[-1].openings)
        for i in old_open:
            if i != opening:
                new_open.append(i)
        self.path[-1].openings = new_open
        print("DELETING {}".format(opening))

    def pop_cell(self):
        return self.path.pop()

################################################################################
# Forward: same_heading, Backward: same_heading
# Right (+1), Left(-1)
# N(0) W()

class BOT:
    def __init__(self, curr_loc = 25, heading = 0):
        self.prev_cell_no = -1
        self.curr_cell_no = curr_loc
        self.heading = heading

    def dest_cell_no(self, direction):
        current_cell_no = self.curr_cell_no

        if direction == 0:
            dest_cell_no = current_cell_no - 7
        elif direction == 1:
            dest_cell_no = current_cell_no + 1
        elif direction == 2:
            dest_cell_no = current_cell_no + 7
        elif direction == 3:
            dest_cell_no = current_cell_no - 1

        return dest_cell_no

    def forward_move(self, from_cell, to_cell):
        bot_heading = self.heading
        diff = to_cell - from_cell

        if diff == -7:
            move_dir = 0
        elif diff == 7:
            move_dir = 2
        elif diff == 1:
            move_dir = 1
        elif diff == -1:
            move_dir = 3

        print("DIFF:  {}".format(move_dir - bot_heading))
        print("BOT PREV HEADING {}".format(self.heading))
        if abs(move_dir - bot_heading) == 0:
            # move_forward_method()
            self.heading = self.heading
            print("MOVEVING FORWARD")
        elif abs(move_dir - bot_heading) == 2:
            # move_backward_method()
            self.heading = self.heading
            print("MOVEVING BACKWARD")
        elif move_dir - bot_heading == 1 or move_dir - bot_heading == -3:
            # move_right_method()
            self.heading = (self.heading + 1) % 4
            print("MOVEVING FORWARD-RIGHT")
        elif move_dir - bot_heading == -1 or move_dir - bot_heading == 3:
            self.heading = (self.heading - 1) % 4
            print("MOVEVING FORWARD-LEFT")
            # move_left_method()

        print("BOT CURR HEADING {}".format(self.heading))

        self.prev_cell_no = from_cell
        self.curr_cell_no = to_cell

    def revert_move(self, from_cell, to_cell):
        bot_heading = self.heading
        diff = to_cell - from_cell

        if diff == -7:
            move_dir = 0
        elif diff == 7:
            move_dir = 2
        elif diff == 1:
            move_dir = 1
        elif diff == -1:
            move_dir = 3

        print("DIFF:  {}".format(move_dir - bot_heading))
        print("BOT PREV HEADING {}".format(self.heading))
        if abs(move_dir - bot_heading) == 0:
            # move_forward_method()
            self.heading = self.heading
            print("MOVEVING FORWARD")
        elif abs(move_dir - bot_heading) == 2:
            # move_backward_method()
            self.heading = self.heading
            print("MOVEVING BACKWARD")
        elif move_dir - bot_heading == 1 or move_dir - bot_heading == -3:
            # move_right_method()
            self.heading = (self.heading - 1) % 4
            print("MOVEVING BACKWARD-RIGHT")
        elif move_dir - bot_heading == -1 or move_dir - bot_heading == 3:
            self.heading = (self.heading + 1) % 4
            print("MOVEVING BACKWARD-LEFT")
            # move_left_method()

        print("BOT CURR HEADING {}".format(self.heading))

        self.prev_cell_no = from_cell
        self.curr_cell_no = to_cell


    def take_measurements(self, cell_no):
        test_maze_xxx = {9: [], 10: [2,3,0],  11:[3],
                         16: [0], 17: [3], 18: [0],
                         23: [], 24: [3], 25:[0,3]}


        # Here, if measurements are in certain distance, replace with opening or closing.
        msmt = test_maze_xxx[cell_no]
        return msmt

################################################################################
# START GAME
iter_cnt = 0
test_bot = BOT()
bot_position = test_bot.curr_cell_no
print("BOT STARTING IN CELL:  {}\n\n".format(bot_position))

sensor_measurements = test_bot.take_measurements(bot_position)
print("BOT POSSIBLE MOVES:    {}".format(sensor_measurements))

new_cell = CELL(bot_position, open_dir = sensor_measurements)
test_path = PATH(new_cell)
test_path.print_path()


while -1 not in sensor_measurements:
    iter_cnt += 1

    # CASE - Dead-end: REVERTING IN CASE OF ENCOUNTERING DEAD END.
    while len(sensor_measurements) == 0:
        # First mark the dead-end as dead-cell for current location
        print("\t*****======>{}<======*****".format(iter_cnt))
        print("\tBOT REVERTING MOVES!")
        # Pop out the most recently added cell(dead-end) and take current bot location.
        current_cell = test_path.pop_cell()
        bot_position = current_cell.cell_no
        print("\tBOT REVETTING FROM CELL  {}".format(bot_position))

        # Grabbing the cell before the dead-end and cell number.
        revert_cell = test_path.most_recent_cell()
        revert_cell_no = revert_cell.cell_no
        print("\tBOT REVERTING TO:        {}".format(revert_cell_no))

        # Revert from dead-end to the previous cell.
        test_bot.revert_move(bot_position, revert_cell_no)
        print("\tBOT COMPLETED MOVING")

        # Grab the bot's current cell number
        bot_position = test_bot.curr_cell_no
        bot_heading = test_bot.heading
        print("\tBOT NOW IN CELL:         {}".format(bot_position))
        print("\tBOT HEADING IS :         {}".format(bot_heading))

        # Print out the path and x-map
        stdout.write("\t")
        test_path.print_path()

        # Grab new sensor measurements to find another opening.
        sensor_measurements = test_path.most_recent_cell().openings
        iter_cnt +=1
        print("\t*****======*****======*****\n")

    # CASE - No dead-end
    print("===========>{}<=============".format(iter_cnt))
    print("BOT MOVING FROM CELL:    {}".format(test_bot.curr_cell_no))
    print("BOT POSSIBLE MOVES:      {}".format(sensor_measurements))

    # Pick one direction from MANY: HERE using the logic that moving forward to the same direction is least error-prone
    # Also assuming sensor measurement is taken by [Center, Left, Right]
    exit_dir = test_path.check_exit_avail(test_bot.curr_cell_no, sensor_measurements)
    if type(exit_dir) == int:
        move_to_dir = exit_dir
        print("MOVE TO DIRECTION SET AS {}".format(move_to_dir))
    elif type(exit_dir) == bool:
        move_to_dir = sensor_measurements[0]

    # Get the cell number that results from moving one cell to the selectd direction.
    print("BOT TAKING DIRECTION:    {}".format(move_to_dir))
    dest_cell = test_bot.dest_cell_no(move_to_dir)

    print("BOT MOVING TO CELL:      {}".format(dest_cell))



    # First delete the direction from the possible direction list
    test_path.delete_opening(move_to_dir)

    test_bot.forward_move(test_bot.curr_cell_no, dest_cell)
    if type(exit_dir) == int:
        print("Game Done")
        break
    ### NEW*
    test_path.add_visited(dest_cell)
    ### NEW* Check for "Bingo"
    test_path.check_bingo_and_update_exit_cells()

    print("BOT COMPLETED MOVING")

    # Print the cell number after bot moving
    bot_position = test_bot.curr_cell_no
    bot_heading = test_bot.heading
    print("BOT NOW IN CELL:         {}".format(bot_position))
    print("BOT HEADING IS :         {}".format(bot_heading))

    # Take new sensor measurements
    sensor_measurements = test_bot.take_measurements(bot_position)
    # Create a new cell to store information.
    new_cell = CELL(bot_position, open_dir = sensor_measurements)
    # Append to current test_path
    test_path.append_cell(new_cell)
    test_path.print_path()
    print("==========================\n")
    if iter_cnt == 10:
        break
test_path.mark_map_end(bot_position, test_bot.heading)



test_maze_0 = {1: [-1], 2: [3], 3:[3],
               6: [-1, 0], 7: [1], 8: [0],
               11: [0], 12: [0,3], 13:[3]}

test_maze_1 = {1: [2], 2: [3], 3:[3],
               6: [-1], 7: [1], 8: [0],
               11: [], 12: [0,3], 13:[3]}

test_maze_2 = {1: [2], 2: [1,3], 3:[2],
               6: [2], 7: [0], 8: [2],
               11: [], 12: [0], 13:[-1]}

test_maze_x = {3: [1], 4: [1,2], 5:[],
               8: [0], 9: [2, 1], 10: [-1],
               13: [0, 1], 14: [1,3], 15:[]}

test_maze_xxx = {1: [-1], 2: [],  3:[],
                 6: [0], 7: [0, 2, 3], 8: [0, 3],
                 11: [], 12: [3], 13:[0]}

test_maze_xxx = {1: [-1], 2: [],  3:[],
                 6: [0], 7: [0, 2, 3], 8: [0, 3],
                 11: [], 12: [3], 13:[0]}
