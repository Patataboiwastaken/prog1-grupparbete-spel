import stats
map_size_x = 13
map_size_y = 15
map = []
for i in range(0,map_size_y):
    map.append([])

for y in range(0,map_size_y):
    output_line = []
    curr_line = input(f"Input line {y}: ")
    for x in curr_line:
        for entity in stats.list_of_entity_types:
            if entity.entity_type == "chest":
                if x == entity.name:
                    map[y].append(("stats.chest"+entity.name))
            else:
                if x == entity.map_icon:
                    map[y].append(("stats."+entity.name))

map_temp = str(map)
map = ""
for i in map_temp:
    if not i == "'":
        map += i

print(map)

