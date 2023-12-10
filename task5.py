import numpy as np
import pandas as pd

# import file
with open('input5.txt', 'r') as f:
    lines = f.read()

instructions = lines.split('\n\n')

# parse instructions
maps = {x.replace(' map', ''): list(map(lambda x: list(map(int, x.split())), y.strip().split('\n'))) for instruction in
        instructions for x, y in [instruction.split(':')]}
seeds = maps.pop('seeds')[0]

# define index for source, destination and step
i_source, i_dest, step = 1, 0, 2

# prepare dataframe for mappings (only relevant seeds)
col_names = pd.Series(
    [item for sublist in map(lambda x: x.split('-to-'), maps.keys()) for item in sublist]).drop_duplicates().tolist()
mappings = pd.DataFrame({col_name: [np.nan] * len(seeds) for col_name in col_names})
mappings['seed'] = seeds


def create_mapping(mappings: pd.DataFrame, single_map: list[list[int]], map_name: str) -> pd.DataFrame:
    name_from, name_to = map_name.split('-to-')
    # copy values from source to destination
    mappings.loc[mappings[name_to].isna(), name_to] = mappings[name_from]
    for line in single_map:
        # optimised version
        for value_category_from in mappings[name_from].to_list():
            min_from, max_from = line[i_source], line[i_source] + line[step] - 1
            # check if mapping affects relevant seed
            if min_from <= value_category_from <= max_from:
                diff = value_category_from - min_from
                # update value
                mappings.loc[mappings[name_from] == value_category_from, name_to] = line[i_dest] + diff

        # slow version
        # for i in range(line[step]):
        # mappings.loc[mappings[name_from] == (line[i_source] + i), name_to] = line[i_dest] + i

    return mappings


# loop though all maps
for map_name in maps:
    mappings = create_mapping(mappings, maps[map_name], map_name)

# get minimum location
min_location = mappings['location'].min()
print(f'Min location: {int(min_location)}')
