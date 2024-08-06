area_loops = 4
length = get_world_size() 
area = length * length
seed_count = area * 1.2 * 1.1
total_coulmn_runs = length * area_loops
safety_margin = 1.1
while True:
	planted_count = 0
	while planted_count < area * safety_margin:
			for i in range(length):
				if get_entity_type() == Entities.Pumpkin:
					planted_count += 1
				else:
					planted_count = 0
				p("pumpkin")
				move(North)
			move(East)	
	harvest()
	