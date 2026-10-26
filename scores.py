"""Persistent win/loss/draw tracking."""
import json
from pathlib import Path

SCORE_FILE = Path(__file__).with_name("scores.json")
DEFAULT = {"wins": 0, "losses": 0, "draws": 0}


def load():
    try:
        return {**DEFAULT, **json.loads(SCORE_FILE.read_text())}
    except (FileNotFoundError, json.JSONDecodeError):
        return dict(DEFAULT)


def save(scores):
    SCORE_FILE.write_text(json.dumps(scores, indent=2))


def record(scores, result):
    """result: 'win' | 'loss' | 'draw' (from the human's perspective)."""
    scores[{"win": "wins", "loss": "losses", "draw": "draws"}[result]] += 1
    save(scores)
