def generate_mazes(mazes, current_maze):
    if len(current_maze) == 49:
        mazes.append(current_maze)
        return

    # Are we at a fixed point?
    fixed_points = [0, 2, 4, 6, 14, 16, 18, 20, 28, 30, 32, 34, 42, 44, 46, 48]
    addition = False
    for fixed_point in fixed_points:
        if fixed_point == len(current_maze):
            addition = True
            generate_mazes(mazes, current_maze + '1')

    # Are we at an edge where the car can exit?
    if not addition:
        edge_locations = [1, 3, 5, 7, 13, 21, 27, 35, 41, 43, 45, 47]
        edges = ''
        addition = False
        for edge_location in edge_locations:
            if edge_location < len(current_maze):
                edges += current_maze[edge_location]
            elif edge_location == len(current_maze):
                addition = True
                if edges.count('0') < 2:
                    generate_mazes(mazes, current_maze + '0')
                if edge_location < 45 or (edge_location == 45 and edges.count('0') >= 1) or (edge_location == 47 and edges.count('0') == 2):
                    generate_mazes(mazes, current_maze + '1')

    # Internal walls
    if not addition:
        internal_walls = [9, 11, 15, 17, 19, 23, 25, 29, 31, 33, 37, 39]
        walls = ''
        addition = False
        for internal_wall in internal_walls:
            if internal_wall < len(current_maze):
                walls += current_maze[internal_wall]
            elif internal_wall == len(current_maze):
                addition = True
                if walls.count('1') < 4:
                    generate_mazes(mazes, current_maze + '1')
                if internal_wall < 31 or (internal_wall == 31 and walls.count('1') >= 1) or (internal_wall == 33 and walls.count('1') >= 2) or (internal_wall == 37 and walls.count('1') >= 3) or (internal_wall == 39 and walls.count('1') == 4):
                    generate_mazes(mazes, current_maze + '0')

    # All that is left is empty space
    if not addition:
        generate_mazes(mazes, current_maze + '0')

def print_maze(maze):
    for i in range(0, 49, 7):
        print(maze[i:(i + 7)])
    print('-------')

mazes = []
generate_mazes(mazes, '')

i = 0
for maze in mazes[0:5]:
    i += 1
    print_maze(maze)
    print(type(maze))
