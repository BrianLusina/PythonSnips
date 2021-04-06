def square_odds(num_list):
    sq = [str(int(x) ** 2) for x in num_list.split(",") if int(x) % 2 != 0]
    return ",".join(sq)
