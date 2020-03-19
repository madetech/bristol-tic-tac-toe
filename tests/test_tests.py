class Board(object):
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

class GetBoard(object):
    def __init__(self, board):
        self.board = board

    def execute(self):
        return self.board.board

class PlacePiece:
    def __init__(self, board):
        self.board = board

    def execute(self, x, y):
        if self.board.board[x][y] is not None:
            return False
        self.board.board[x][y] = 'X'
        return True

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
        [None, 'X', None],
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

def test_someone_cannot_place_piece_in_square_that_is_taken():
    board = Board()
    PlacePiece(board).execute(2, 0)
    success = PlacePiece(board).execute(2, 0)
    assert success == False

def test_when_someone_places_x_success_is_returned():
    board = Board()
    success = PlacePiece(board).execute(2, 0)
    assert success == True
