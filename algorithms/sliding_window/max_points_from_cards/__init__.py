from typing import List


def max_score(card_points: List[int], k: int) -> int:
    number_of_cards = len(card_points)
    total_points = sum(card_points)

    # If we have to pick all the cards or more cards that we have been provided with, then the max score is the total
    # of all the cards
    if k >= number_of_cards:
        return total_points

    # Maintain a state or the window sum to calculate the sum of the cards in the window
    window_sum = 0
    # Max points is the score we get from the cards we pick, this is what we eventually return
    max_points = 0
    # This will keep track of the index of the card to remove from the current window as we traverse the cards
    start = 0

    for end in range(number_of_cards):
        # Add the card at the end of the window to the window sum
        window_sum += card_points[end]

        # Calculates if we have a valid window to calculate the max points
        if end - start + 1 == number_of_cards - k:
            max_points = max(max_points, total_points - window_sum)
            # Contract the window, by removing the card at the start of the window
            window_sum -= card_points[start]
            # Move to the next index
            start += 1

    return max_points
