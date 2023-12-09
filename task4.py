import re

# import file
with open('input4.txt', 'r') as f:
    cards = f.readlines()


def get_number_of_matches(card: str) -> int:
    # split to winning and my numbers
    _, winning_num, my_num = re.split(r': | \| ', card)
    winning_num, my_num = list(map(int, winning_num.split())), list(map(int, my_num.split()))
    # get number of matching numbers
    n_matches = len(set(winning_num).intersection(set(my_num)))
    return n_matches


# part 1
# sum points for each card (2^(n_matches - 1))
points = sum(int(2 ** (get_number_of_matches(card) - 1)) for card in cards)
print(f'Points total: {points}')

# part 2
cards_n = {i: 1 for i in range(1, len(cards) + 1)}  # counter for each card
for card_i in range(1, len(cards) + 1):  # for each card
    n_matches = get_number_of_matches(cards[card_i - 1])  # get number of matches
    copies = [card_i + i + 1 for i in range(n_matches)]  # get indices of copies
    for copy in copies:  # add copies to counter
        cards_n[copy] += cards_n[card_i]

print(f'Scratchcards total: {sum(cards_n.values())}')
