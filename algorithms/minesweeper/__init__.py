class Minesweeper(object):
    """
    Minesweeper class
    """

    def __init__(self):
        pass

    def board(self, inp):
        """
        Adds the numbers to a minesweeper board
        :param inp: input board
        :return:board with the numbers displayed
        :rtype:list
        """
        # check if the board is valid
        self.verify_board(inp)

        # get the row length
        row_len = len(inp[0])
        # get the column length
        col_len = len(inp)

        b = [list(r) for r in inp]

        for i1 in range(col_len):
            for i2 in range(row_len):
                if b[i1][i2] != ' ':
                    continue
                cnt = inp[i1 - 1][i2 - 1:i2 + 2].count('*') + \
                      inp[i1][i2 - 1:i2 + 2].count('*') + \
                      inp[i1 + 1][i2 - 1:i2 + 2].count('*')
                if cnt == 0:
                    continue
                b[i1][i2] = str(cnt)
        return ["".join(r) for r in b]

    @staticmethod
    def verify_board(inp):
        """
        validates its input and raise a ValueError with a meaningful error message
        if the input turns out to be malformed.
        :param inp: The input board
        :raises: ValueError
        """
        # Null board or a null row
        if not inp or not all(r for r in inp):
            raise ValueError("Invalid board")

        # Rows with different lengths
        row_len = len(inp[0])
        col_len = len(inp)
        if not all(len(r) == row_len for r in inp):
            raise ValueError("Invalid board")

        # Unknown character in board
        c_set = set()
        for r in inp:
            c_set.update(r)
        if c_set - set('+- *|'):
            raise ValueError("Invalid board")

        # Borders not as expected
        if any(inp[i1] != '+' + '-' * (row_len - 2) + '+' for i1 in [0, -1]) or \
                any(inp[i1][i2] != '|' for i1 in range(1, col_len - 1) for i2 in [0, -1]):
            raise ValueError("Invalid board")
