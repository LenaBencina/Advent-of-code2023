import re

# import file
with open('input1.txt', 'r') as f:
    lines = f.readlines()

# word to digit mapping
word_to_int = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# initialize for final results
sum_calibration1, sum_calibration2 = 0, 0

for line in lines:
    line = line.strip()

    # PART 1
    # get digits from line
    numbers = list(filter(lambda x: x.isdigit(), line))
    # sum first and last digit
    calibration_value = int(numbers[0] + numbers[len(numbers) - 1])
    # add to final sum
    sum_calibration1 += calibration_value

    # PART 2
    # concatenate all possible substrings
    all_digits_string = '|'.join(list(word_to_int.keys()) + list(word_to_int.values()))
    # find any of it in line
    numbers2 = re.findall(f'(?=({all_digits_string}))', line)
    # extract first and last number
    first, last = numbers2[0], numbers2[len(numbers2) - 1]
    # convert word digits if necessary
    digits_to_sum = list(map(lambda x: x if not word_to_int.get(x) else word_to_int[x], [first, last]))
    # add to final sum (concatenate digits and convert to int)
    sum_calibration2 += int(''.join(digits_to_sum))

print(f'Sum 1: {sum_calibration1}')
print(f'Sum 2: {sum_calibration2}')
