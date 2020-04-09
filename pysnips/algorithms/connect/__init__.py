class ConnectGame:
    """
    :cvar directions denotes movement of a player on the board
    :cvar player_o denotes player O
    :cvar player_x denotes player X
    :cvar none indicates a tie, no player won
    """

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    player_o = "O"
    player_x = "X"
    none = ""

    def __init__(self, board):
        self.board = ConnectGame.make_board(board)

        if len(self.board) <= 0:
            raise Exception("Expected Board to be greater than 0")

        self.width = len(self.board[0])
        self.height = len(self.board)

        if self.width <= 0 and self.height <= 0:
            raise Exception("Expected width and height of board to be greater than 0")

        for line in self.board:
            assert len(line) == self.width

    @staticmethod
    def make_board(lines: str) -> list:
        """
        Makes the board by splitting each line on the string and joining them into a list
        :param lines: Board
        :type lines str
        :return: List of lines from the board
        :rtype: list
        """
        return ["".join(line.split()) for line in lines.splitlines()]

    def valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def has_player_reach_destination(self, player, x, y) -> bool:
        """
        Checks if a player has reached their destination
        :param player: Either player_x or player_o
        :param x: X point
        :param y: Y point
        :return: True if either player has reached their destination
        """
        if player == self.player_x:
            return x == self.width - 1
        if player == self.player_o:
            return y == self.height - 1

    def walk_board(self, player, x, y, visited=None):
        if visited is None:
            visited = []
        if (x, y) in visited:
            return False

        if (not self.valid(x, y)) or self.board[y][x] != player:
            return False

        if self.has_player_reach_destination(player, x, y):
            return True

        for d in self.directions:
            if self.walk_board(player, x + d[0], y + d[1], visited + [(x, y)]):
                return True

    def check_player_is_winner(self, player: str) -> bool:
        """
        Checks if a player is the winner. Accepts a player parameter, either (player_x or player_o) and returns boolean
        if either is the winner
        :param player: Either cvar player_o or player_x
        :type player str
        :return: True/False if player_x or player_o is a winner
        :rtype: bool
        """

        if player == self.player_x:
            for y in range(self.height):
                if self.walk_board(player, 0, y):
                    return True

        if player == self.player_o:
            for x in range(self.width):
                if self.walk_board(player, x, 0):
                    return True

    def get_winner(self):
        if self.check_player_is_winner(self.player_x):
            return self.player_x
        if self.check_player_is_winner(self.player_o):
            return self.player_o
        return self.none
