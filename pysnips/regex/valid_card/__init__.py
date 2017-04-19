def valid_card(card):
    return not sum([d if i & 1 else d % 5 * 2 + d / 5 for i, d in enumerate(map(int, card.replace(" ", "")))]) % 10
