class Board(object):
    def __init__(self):
        self.piece_placed = False


class GetBoard(object):
    def __init__(self, board):
        self.board = board

    def execute(self):
        presentable_board = [[None, None, None], [None, None, None], [None, None, None]]
        if self.board.piece_placed:
            presentable_board[1][1] = 'X'
        return presentable_board

class PlacePiece:
    def __init__(self, board):
        self.board = board

    def execute(self, x, y):
        self.board.piece_placed = True


def test_at_the_start_of_the_game_the_board_is_empty():
    board = Board()
    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def test_someone_can_place_an_x_in_the_middle_of_the_board():
    board = Board()
    PlacePiece(board).execute(1, 1)

    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, "X", None],
        [None, None, None],
    ]

def test_someone_can_place_x_in_the_bottom_left_corner():
    board = Board()
    PlacePiece(board).execute(2, 0)

    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, None, None],
        ['X', None, None],
    ]