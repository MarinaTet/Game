import pytest
from tic_tac_toe import evaluate, move

# Test cases for evaluate
@pytest.mark.parametrize("board, expected", [
    ("xxx-----------------", 'x'),  # Player wins
    ("ooo-----------------", 'o'),  # PC wins
    ("xoxoxoxoxoxoxoxoxoxo", '!'),  # Draw
    ("xoxoxoxoxoxoxoxoxox-", '-'),  # Game ongoing
])
def test_evaluate(board, expected):
    assert evaluate(board) == expected

# Test cases for move
@pytest.mark.parametrize("board, mark, position, expected", [
    ("--------------------", 'x', 0, "x-------------------"),  # Place 'x' at position 0
    ("x-------------------", 'o', 1, "xo------------------"),  # Place 'o' at position 1
])
def test_move(board, mark, position, expected):
    assert move(board, mark, position) == expected
