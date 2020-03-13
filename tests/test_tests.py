class GetBoard(object):
    def execute(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]


def test_at_the_start_of_the_game_the_board_is_empty():
    assert GetBoard().execute() == [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

# def test_