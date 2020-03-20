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

    def execute(self, x, y, piece):
        is_square_empty = self.board.board[x][y] is None

        if is_square_empty:
            self.board.board[x][y] = piece
        return is_square_empty


def test_at_the_start_of_the_game_the_board_is_empty():
    board = Board()
    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def test_someone_can_place_an_x_in_the_middle_of_the_board():
    board = Board()
    PlacePiece(board).execute(1, 1,'X')

    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, 'X', None],
        [None, None, None],
    ]

def test_someone_can_place_x_in_the_bottom_left_corner():
    board = Board()
    PlacePiece(board).execute(2, 0,'X')

    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, None, None],
        ['X', None, None],
    ]

def test_when_someone_places_x_success_is_returned():
    board = Board()
    success = PlacePiece(board).execute(2, 0,'X')
    assert success == True

def test_placing_in_a_taken_location_is_invalid():
    board = Board()
    PlacePiece(board).execute(2, 0,'X')
    success = PlacePiece(board).execute(2, 0,'X')
    assert success == False

def test_cannot_place_piece_in_square_that_is_taken_by_other_player():
    board = Board()
    PlacePiece(board).execute(2, 0,'X')
    success = PlacePiece(board).execute(2, 0,'O')
    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, None, None],
        ['X', None, None],
    ]

def test_someone_can_place_o_on_board():
    board = Board()
    PlacePiece(board).execute(1,1,'O')
    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, 'O', None],
        [None, None, None],
    ]

def test_that_we_can_view_the_board():
    view_board = BoardPrinter(GetBoard(Board()))
    view_board.execute()


