from __builtins__ import *
from Functions import *

def maze_move(old_orientation = 0):
    direction_names = [North, East, South, West]
    for direction_raw in range(-1, 3):
        direction_corrected = (old_orientation + direction_raw) % 4
        direction_name = direction_names[direction_corrected]
        quick_print(direction_raw,direction_corrected)
        # quick_print('attempting to move', direction_name)
        if move(direction_name):
            new_orientation = direction_corrected
            # quick_print('success', direction_name)
            return new_orientation

while True:
    goto_start()
    spawn_maze()

    orientation = 0
    for step in range(200):
        orientation = maze_move(orientation)
        treasure = get_entity_type() == Entities.Treasure
        if treasure:
            harvest()
            break