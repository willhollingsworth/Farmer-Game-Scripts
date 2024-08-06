goto_start()
length = get_world_size() 
while True:
	for i in range(length):
		x = get_pos_x()
		y = get_pos_y() 
		even_x = x % 2 == 0
		even_y = y % 2 == 0
		if (even_x and even_y) or (not even_x and not even_y):
			p("tree")
		else:
			p("grass")
		move(North)
	move(East)	
	