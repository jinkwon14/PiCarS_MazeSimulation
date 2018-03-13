import numpy as np
import copy

class MAZE:
    def __init__(self):
        self.maze = np.zeros((3,3,5))
        # maze[0] = (V)isited: 1 = visited, 0 = not visited
        # maze[1] = (D)ifferent Move?: # of different moves
        # maze[2] = (X) dead cell

        self.maze_printable = np.zeros((3,5))

    def print_maze(self):
        for row in self.maze_printable:
            print(row)
        print("--------------------------")

    def init_maze(self, init_loc):
        init_y = init_loc[0]
        init_x = init_loc[1]
        self.maze_printable[init_x, init_y] = 7

    def update_maze_param(self, old_lo, new_lo):
        x_loc_to = new_lo[1]
        y_loc_to = new_lo[0]
        x_loc_from = old_lo[1]
        y_loc_from = old_lo[0]
        print("MOVE TO {}",format(str(new_lo)))
        print("MOVE FROM {}",format(str(old_lo)))

        self.maze[0][x_loc_from, y_loc_from] = 1
        self.maze[1][x_loc_from, y_loc_from] = 2
        self.maze[2][x_loc_from, y_loc_from] = 0


    def update_maze_look(self, loc_prev, loc_curr):
        x_loc_to = loc_curr[1]
        y_loc_to = loc_curr[0]
        x_loc_from = loc_prev[1]
        y_loc_from = loc_prev[0]
        self.maze_printable[x_loc_from, y_loc_from] = 1
        self.maze_printable[x_loc_to, y_loc_to] = 7

    def check_maze_size(self):
        return True

        
class BOT:
    def __init__(self, loc = [2, 0]):
        self.curr_loc = loc

    def move(self, move_to):
        if move_to == "F":
            self.curr_loc[1] += 1
        elif move_to == "B":
            self.curr_loc[1] -= 1
        elif move_to == "R":
            self.curr_loc[0] += 1
        elif move_to == "L":
            self.curr_loc[0] -= 1
        else:
            print("invalid move")

    def turn(self, direction):
        if direction == "F":
            # do soething
        elif direction == "L":
            # do something else
        else:
            print("WRONG DIRECTION INPUT!")

    def take_measurement(self):
        left_msrmt = raw_input("Left Measurement: ")
        right_msrmt = raw_input("Right Measurement: ")
        center_msrmt = raw_input("Center Measurement: ")
        return [left_msrmt, right_msrmt, center_msrmt]


    def check_move(self, move_to):
        print("Checking Bot Move currently at{}".format(self.curr_loc))
        if move_to == "F":
            test_loc = [self.curr_loc[0] + 1, self.curr_loc[1]]
        elif move_to == "B":
            test_loc = [self.curr_loc[0] - 1, self.curr_loc[1]]
        elif move_to == "R":
            test_loc = [self.curr_loc[0], self.curr_loc[1] + 1]
        elif move_to == "L":
            test_loc = [self.curr_loc[0], self.curr_loc[1] - 1]
        else:
            print("invalid move")

        bot_x = test_loc[1]
        bot_y = test_loc[0]

        # if bot_x < 1 or bot_x > 5 or bot_y < 1 or bot_y > 5:
        #     return False
        # else:
        #     return True
        return True

class GAME_GO:
    def __init__(self, maze, bot):
        self.maze = maze
        self.bot = bot

    def ask_move(self):
        move = raw_input("Please enter the number where you wanna move your bot: ")
        return move

    def play(self):
        print("GAME STARTED")
        print("INITIAL BOT POSITION: {}".format(self.bot.curr_loc))
        self.maze.init_maze(self.bot.curr_loc)
        self.maze.print_maze()


        while True:
            move_to = self.ask_move()
            if self.bot.check_move(move_to) == True:
                old_loc = copy.deepcopy(self.bot.curr_loc)
                print("IS THIS UPDATED HERE? {}".format(old_loc))
                self.bot.move(move_to)
                new_loc = self.bot.curr_loc

            self.maze.update_maze_param(old_loc, new_loc)
            self.maze.update_maze_look(old_loc, new_loc)
            self.maze.print_maze()



# Test
board = MAZE()
bot = BOT()
my_game = GAME_GO(board, bot)
my_game.play()









                                                                #
                                                                # class BOT:
                                                                #     def __init__(self, loc = (6, 1), bot_look):
                                                                #         self.curr_loc = loc
                                                                #         self.bot_look = "<[00]>"
                                                                #
                                                                #     def move(self, direction):
                                                                #         if direction == "F":
                                                                #             self.curr_loc =
                                                                #         elif direction == "L":
                                                                #             self.curr_loc =
                                                                #         elif direction == "R":
                                                                #             self.curr_loc =
                                                                #         elif direction == "B":
                                                                #             self.curr_loc =
                                                                #
                                                                #     def check_move(self, bot_loc, direction):
                                                                #         if direction == "F":
                                                                #             self.curr_loc[1] += 2
                                                                #         elif direction == "L":
                                                                #             self.curr_loc[0] -= 2
                                                                #         elif direction == "R":
                                                                #             self.curr_loc[0] += 2
                                                                #         elif direction == "B":
                                                                #             self.curr_loc[1] -= 2
                                                                #
                                                                #         bot_loc_x = self.curr_loc[0]
                                                                #         bot_loc_y = self.curr_loc[1]
                                                                #
                                                                #         if bot_loc_x < 1 or bot_loc_x > 5 or bot_loc_y < 1 or bot_loc_y > 5 or :
                                                                #             print("Invalid Move! Bump to wall!")
                                                                #             return False
                                                                #         else
                                                                #             return True
                                                                #
                                                                #
                                                                #
                                                                # class GAME(object):
                                                                #     def __init__(self, maze, bot):
                                                                #         self.iter = 0
                                                                #         self.maze = maze
                                                                #         self.bot = bot
                                                                #
                                                                #     def print_board(maze):
                                                                #         maze.print_maze()
                                                                #
                                                                #     def ask_input():
                                                                # 		move = raw_input("Please enter the direction where you wanna move: ")
                                                                #         return move
                                                                #
                                                                #
                                                                #     def play(self):
                                                                #         game_over = False
                                                                #         while !game_over:
                                                                #             # Print Maze
                                                                #             self.maze.print_maze()
                                                                #
                                                                #             # Ask for input
                                                                #             dire = self.ask_input()
                                                                #             self.bot.move(dire)
                                                                #             #self.bot.
                                                                #
                                                                #
                                                                # 			currplayer = self.players[self.turn]
                                                                # 			#print board
                                                                # 			self.board.print_board()
                                                                # 			#great user
                                                                # 			self.greet_user(currplayer)
                                                                # 			#ask for move
                                                                # 			move = Move(self.board, currplayer)
                                                                # 			player_move = move.ask_for_move()
                                                                # 			#move - switch board number to player symbol
                                                                # 			self.board.tiles[player_move] = currplayer.symbol
                                                                # 			#checks for a win
                                                                # 			winner = self.check_win(currplayer.symbol)
                                                                # 			#if win, declare win and break loop
                                                                # 			if winner != False:
                                                                # 				self.game_over(winner)
                                                                # 				flag = True
                                                                # 			#else, switch turns by flipping index in self.players array
                                                                # 			else:
                                                                # 				self.turn = 1 - self.turn
                                                                #
