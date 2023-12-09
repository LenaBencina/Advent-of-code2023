import re

# import file
with open('input3.txt', 'r') as f:
    lines = f.readlines()

sum_numbers = 0
for row_number in range(len(lines)):

    line = lines[row_number].strip()

    # find all numbers in line
    numbers_match = list(re.finditer(r'(\d+)', line))

    # for each number
    for match in numbers_match:

        # find positions (x) that need to be checked
        position = match.span()
        start, end = position[0], position[1]
        check_from, check_to = max(start-1, 0), min(end+1, len(line))

        # define string to check in the current line
        to_check = line[check_from:check_to]

        # add string to check from previous and next line if they exist
        if row_number != 0:
            previous_line = lines[row_number - 1]
            to_check += previous_line[check_from:check_to]
        if row_number != len(lines) - 1:
            next_line = lines[row_number + 1]
            to_check += next_line[check_from:check_to]

        # check if symbols in string
        if bool(re.search(r'[^0-9.]', to_check)):
            sum_numbers += int(match.group())

print(f'Sum of numbers: {sum_numbers}')

