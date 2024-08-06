from __builtins__ import *
from Functions import *

length = get_world_size() 
area = length * length
safety_margin = 1.1
area = area * safety_margin
highest_petals = 0
current_petals = 0
all_grown = False
planted_count = 0
ready_for_harvest = False
quick_print('sunflower logic')
quick_print('area size :', area)

while True:
    while not ready_for_harvest:
        for i in range(length):
            if get_entity_type() == Entities.Sunflower:
                planted_count += 1
                current_petals = measure()
                highest_petals = max(highest_petals, current_petals)
                ready_for_harvest = all_grown and current_petals == highest_petals
            else:
                planted_count = 0
                p("sunflower")
            if ready_for_harvest:
                break
            move(North)
        if not ready_for_harvest:
            move(East)	
        all_grown = planted_count > area 
        # quick_print('row complete',all_grown, highest_petals, planted_count, ready_for_harvest)
    quick_print('harvest ready, current petal:',current_petals,' ,highest petal:', highest_petals, ' ,plant count:', planted_count)
    all_grown = False
    ready_for_harvest = False
    highest_petals = 0
    harvest()
	
	