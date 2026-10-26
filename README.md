# AI-Based Tic-Tac-Toe (Minimax)

An unbeatable Tic-Tac-Toe opponent built in Python using the **Minimax algorithm with alpha-beta pruning**.

## Features
- Optimal decision-making via Minimax (the AI never loses; best you can do is draw)
- Alpha-beta pruning for efficient search
- Two interfaces: **CLI** and **Tkinter GUI**
- Persistent win / loss / draw tracking (`scores.json`)
- Starting player alternates each game
- Tests that exhaustively verify the AI can't be beaten

## Project structure
| File | Purpose |
|------|---------|
| `engine.py` | Board logic + Minimax / alpha-beta |
| `scores.py` | Save and load win/loss/draw stats |
| `cli.py` | Command-line game |
| `gui.py` | Tkinter GUI game |
| `test_engine.py` | Pytest tests |

## Run
```bash
python cli.py   # terminal version
python gui.py   # GUI version
```

## Test
```bash
pip install pytest
pytest
```

## How Minimax works here
The AI simulates every possible future game. It scores a win as `10 - depth`, a loss as `depth - 10`, and a draw as `0`, so it prefers winning sooner and losing later. It assumes you play perfectly, picks the move with the best guaranteed outcome, and alpha-beta pruning skips branches that can't change the result.

**Tech stack:** Python 3, Minimax algorithm
