"""Minimax engine (with alpha-beta pruning) for Tic-Tac-Toe."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]
EMPTY = " "


def new_board():
    return [EMPTY] * 9


def winner(board):
    """Return 'X' or 'O' if someone has won, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def is_draw(board):
    return winner(board) is None and not available_moves(board)


def game_over(board):
    return winner(board) is not None or not available_moves(board)


def minimax(board, depth, is_maximizing, ai, human, alpha=-float("inf"), beta=float("inf")):
    """Score a position from the AI's point of view.

    +10 - depth : AI wins (faster wins score higher)
    depth - 10  : human wins (slower losses score higher)
    0           : draw
    """
    w = winner(board)
    if w == ai:
        return 10 - depth
    if w == human:
        return depth - 10
    if not available_moves(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for move in available_moves(board):
            board[move] = ai
            best = max(best, minimax(board, depth + 1, False, ai, human, alpha, beta))
            board[move] = EMPTY
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # prune
        return best
    else:
        best = float("inf")
        for move in available_moves(board):
            board[move] = human
            best = min(best, minimax(board, depth + 1, True, ai, human, alpha, beta))
            board[move] = EMPTY
            beta = min(beta, best)
            if beta <= alpha:
                break  # prune
        return best


def best_move(board, ai, human):
    """Return the index (0-8) of the optimal move for the AI."""
    best_score, move = -float("inf"), None
    for m in available_moves(board):
        board[m] = ai
        score = minimax(board, 1, False, ai, human)
        board[m] = EMPTY
        if score > best_score:
            best_score, move = score, m
    return move
