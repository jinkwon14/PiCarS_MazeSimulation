import numpy as np

class MAZE:
   def __init__(self):
      self.maze = [ ['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #0
                    ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #1
                    ['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #2
                    ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #3
                    ['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #4
                    ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #5
                    ['c', 'u', 'c', 'u', 'c', 'u', 'c']]    #6

    def print_maze(self):
        for row in self.maze:
            print(row)

    def print_bot(self, bot_loc, botlook):
        self.maze[bot_loc] = botlook


class BOT:
    def __init__(self, loc = (6, 1), bot_look):
        self.curr_loc = loc
        self.bot_look = "<[00]>"

    def move(self, direction):
        if direction == "F":
            self.curr_loc =
        elif direction == "L":
            self.curr_loc =
        elif direction == "R":
            self.curr_loc =
        elif direction == "B":
            self.curr_loc =

    def check_move(self, bot_loc, direction):
        if direction == "F":
            self.curr_loc[1] += 2
        elif direction == "L":
            self.curr_loc[0] -= 2
        elif direction == "R":
            self.curr_loc[0] += 2
        elif direction == "B":
            self.curr_loc[1] -= 2

        bot_loc_x = self.curr_loc[0]
        bot_loc_y = self.curr_loc[1]

        if bot_loc_x < 1 or bot_loc_x > 5 or bot_loc_y < 1 or bot_loc_y > 5 or :
            print("Invalid Move! Bump to wall!")
            return False
        else
            return True



class GAME(object):
    def __init__(self, maze, bot):
        self.iter = 0
        self.maze = maze
        self.bot = bot

    def print_board(maze):
        maze.print_maze()

    def ask_input():
		move = raw_input("Please enter the direction where you wanna move: ")
        return move


    def play(self):
        game_over = False
        while !game_over:
            # Print Maze
            self.maze.print_maze()

            # Ask for input
            dire = self.ask_input()
            self.bot.move(dire)
            #self.bot.


			currplayer = self.players[self.turn]
			#print board
			self.board.print_board()
			#great user
			self.greet_user(currplayer)
			#ask for move
			move = Move(self.board, currplayer)
			player_move = move.ask_for_move()
			#move - switch board number to player symbol
			self.board.tiles[player_move] = currplayer.symbol
			#checks for a win
			winner = self.check_win(currplayer.symbol)
			#if win, declare win and break loop
			if winner != False:
				self.game_over(winner)
				flag = True
			#else, switch turns by flipping index in self.players array
			else:
				self.turn = 1 - self.turn



board = MAZE()
bot = BOT()
test = GAME(board, bot)
