from __builtins__ import *

def p(choice,force_harvest=False):
	#harvest and plant logic
	buffer = 20
	stock = 5000
	ent = ""
	seed_type = False
	non_auto_harvest = [Entities.Pumpkin, Entities.Sunflower]
	non_auto_choice = ['pumpkin', 'sunflower']
	till_plants = ['carrot','pumpkin','sunflower']
	if can_harvest():
		plant_type = get_entity_type()
		if plant_type not in non_auto_harvest:
			harvest()
		elif choice == 'pumpkin' and plant_type != Entities.Pumpkin:
			harvest()
		elif choice == 'sunflower' and plant_type != Entities.Sunflower:
			harvest()
	else:
		if get_entity_type() != Entities.Pumpkin:
			harvest()
	if choice == "bush":
		ent = Entities.Bush
	if choice == "grass":
		ent = Entities.Grass	
	if choice == "tree":
		ent = Entities.Tree
	if choice == "carrot":
		ent = Entities.Carrots
		seed_type = Items.Carrot_Seed
	if choice == "pumpkin":
		ent = Entities.Pumpkin
		seed_type = Items.Pumpkin_Seed
	if choice == "sunflower":
		ent = Entities.Sunflower
		seed_type = Items.Sunflower_Seed
	# seed buying logic
	if seed_type:
		current_seed_count = num_items(seed_type) # type: ignore
		if current_seed_count < buffer:
			need_hay = num_items(Items.Hay) < stock # type: ignore
			need_wood = num_items(Items.Wood) < stock # type: ignore
			need_carrot = num_items(Items.Carrot) < stock # type: ignore
			if need_hay:
				ent = Entities.Grass
				choice = "grass"
			elif need_wood:
				ent = Entities.Bush
				choice = "bush"
			elif need_carrot:
				ent = Entities.Carrots
				choice = "carrot"
				current_seed_count = num_items(Items.Pumpkin_Seed) # type: ignore
			if current_seed_count < buffer:
				trade(seed_type, buffer) # type: ignore

	# till logic
	if choice in till_plants:
		if get_ground_type() == Grounds.Turf:
				till()
	else:
		if get_ground_type() == Grounds.Soil:
				till()
	#plant logix
	plant(ent)
	
def goto_start():
	for i in range(get_pos_x()):
		move(West)
	for i in range(get_pos_y()):
		move(South)	

def gather(item):		
	length = get_world_size()
	while True:
		for i in range(length):
			p(item)
			move(North)
		move(East)

def buy_fertilizer():
	buffer = 20
	stock = 5000
	need_carrot = num_items(Items.Carrot) < stock
	need_fertilizer = num_items(Items.Fertilizer) < buffer
	if need_carrot:
		p('carrot')
	elif need_fertilizer:
		trade(Items.Fertilizer, buffer)

def use_fertilizer():
	buy_fertilizer()
	use_item(Items.Fertilizer)

def spawn_maze():
	# plant bushes
	length = get_world_size() 
	for x in range(length):
		for y in range(length):
			p('bush')
			move(North)
		move(East)
	while True:
		entity_type = get_entity_type()
		if entity_type == Entities.Hedge:
			break
		use_fertilizer()