import re

# import file
with open('input2.txt', 'r') as f:
    lines = f.readlines()

max_cubes = {'red': 12, 'green': 13, 'blue': 14}
sum_ids, sum_power = 0, 0
game_id = 1

for line in lines:
    line = line.strip()

    possible = True
    power_minimum = 1

    # for each color
    for color in ['red', 'green', 'blue']:
        # find all numbers associated with specific color
        all_by_color = re.findall(r'(\d+) ' + re.escape(color), line)

        # check if all numbers are <= max
        possible_tmp = all(int(n_cubes) <= max_cubes[color] for n_cubes in all_by_color)
        if not possible_tmp:
            possible = False

        # find max (i.e. fewest number of cubes) and multiply
        power_minimum *= max(map(int, all_by_color))

    # add id for first part and power for second part
    sum_ids += game_id if possible else 0
    sum_power += power_minimum
    game_id += 1

print(f'Sum of IDs: {sum_ids}')
print(f'Sum of power: {sum_power}')
