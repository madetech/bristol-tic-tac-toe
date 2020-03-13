class GetBoard(object):
    def execute(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]


def test_test():
    assert GetBoard().execute() == [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
