# FIX: Refactored from app.py with Copilot Agent help
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    # FIX: Corrected high/low logic and moved from app.py
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        return "Too Low"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    #FIX: Score formula fixed to be attempt-based and non-negative on win
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    #FIX: Wrong guesses now always penalize -5, no positive score for misses
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
