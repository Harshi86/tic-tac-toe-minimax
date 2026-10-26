"""Proves the AI is unbeatable: explores every possible human move sequence."""
import engine


def human_can_win(board, human, ai, turn):
    if engine.winner(board) == human:
        return True
    if engine.game_over(board):
        return False
    if turn == ai:
        m = engine.best_move(board, ai, human)
        board[m] = ai
        r = human_can_win(board, human, ai, human)
        board[m] = engine.EMPTY
        return r
    for m in engine.available_moves(board):
        board[m] = human
        r = human_can_win(board, human, ai, ai)
        board[m] = engine.EMPTY
        if r:
            return True
    return False


def test_ai_never_loses_as_O():
    assert not human_can_win(engine.new_board(), "X", "O", "X")


def test_ai_never_loses_as_X():
    assert not human_can_win(engine.new_board(), "O", "X", "X")


def test_ai_takes_winning_move():
    b = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
    assert engine.best_move(b, "X", "O") == 2


def test_ai_blocks():
    b = ["O", "O", " ", "X", " ", " ", " ", " ", "X"]
    assert engine.best_move(b, "X", "O") == 2
