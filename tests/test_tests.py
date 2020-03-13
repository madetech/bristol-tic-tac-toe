class Board(object):
    pass

class GetBoard(object):
    def execute(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

class PlacePiece():
    def __init__(self, board):
        pass

    def execute(self, x, y):
        pass

def test_at_the_start_of_the_game_the_board_is_empty():
    assert GetBoard().execute() == [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def test_someone_can_place_an_x_in_the_middle_of_the_board():
    board = Board()
    PlacePiece(board).execute(1, 1)

    assert GetBoard(board).execute() == [
        [None, None, None],
        [None, "X", None],
        [None, None, None]]
