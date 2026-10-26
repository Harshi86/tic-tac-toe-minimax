"""Command-line Tic-Tac-Toe vs. a Minimax AI."""
import engine
import scores as sc


def show(board):
    rows = [" | ".join(board[i:i + 3]) for i in (0, 3, 6)]
    print("\n" + "\n---------\n".join(rows) + "\n")


def show_guide():
    print("Positions:")
    show([str(i + 1) for i in range(9)])


def ask_human_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw) - 1] == engine.EMPTY:
            return int(raw) - 1
        print("Invalid or taken square, try again.")


def play_round(human, ai, human_first):
    board = engine.new_board()
    turn = human if human_first else ai
    show_guide()
    while not engine.game_over(board):
        if turn == human:
            board[ask_human_move(board)] = human
        else:
            board[engine.best_move(board, ai, human)] = ai
            print("AI moves:")
        show(board)
        turn = ai if turn == human else human
    w = engine.winner(board)
    if w == human:
        print("You win!"); return "win"
    if w == ai:
        print("AI wins!"); return "loss"
    print("It's a draw."); return "draw"


def main():
    scores = sc.load()
    print("=== AI Tic-Tac-Toe (Minimax) ===")
    human = ""
    while human not in ("X", "O"):
        human = input("Play as X or O? ").strip().upper()
    ai = "O" if human == "X" else "X"
    human_first = human == "X"

    while True:
        result = play_round(human, ai, human_first)
        sc.record(scores, result)
        print(f"Score -> Wins: {scores['wins']} | Losses: {scores['losses']} | Draws: {scores['draws']}")
        if input("Play again? (y/n): ").strip().lower() != "y":
            break
        human_first = not human_first  # alternate who starts
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
