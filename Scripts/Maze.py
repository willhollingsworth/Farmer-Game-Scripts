from __builtins__ import *
from Functions import *

length = get_world_size() 


# goto_start()
# spawn_maze()
def maze_move(_backtrack_direction):
    directions_names = [North, East, South, West]
    directions = range(4)
    for direction in directions:
        if move(directions_names[direction]) and direction != _backtrack_direction:
            _backtrack_direction = (direction + 2) % 4
            quick_print('moved', direction, 'backtrack', _backtrack_direction)
            return _backtrack_direction
    direction = _backtrack_direction    
    move(direction)
    _backtrack_direction = (direction + 2) % 4
    quick_print('failesafe moved', direction, 'backtrack', _backtrack_direction)
    return _backtrack_direction


backtrack_direction = 0
for x in range(30):
    backtrack_direction = maze_move(backtrack_direction)