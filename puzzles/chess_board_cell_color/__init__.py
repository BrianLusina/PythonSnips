def chess_board_cell_color(cell1, cell2):
    return (ord(cell1[0]) + ord(cell1[1])) % 2 == (ord(cell2[0]) + ord(cell2[1])) % 2
