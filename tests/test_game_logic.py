from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
def test_guess_hints_are_correct_for_direction():
    # Regression test for bug where hints were reversed in app logic.
    secret = 30
    guess_too_low = 20
    guess_too_high = 40

    assert check_guess(guess_too_low, secret) == "Too Low"
    assert check_guess(guess_too_high, secret) == "Too High"
def test_score_updates_for_guesses():
    score = 0
    score = update_score(score, "Too High", 1)
    assert score == -5
    score = update_score(score, "Too High", 2)
    assert score == -10
    score = update_score(score, "Too Low", 3)
    assert score == -15
    score = update_score(score, "Win", 4)
    assert score == -15 + 60    #FIX: Score for win should be 100 - 10 * attempt_number (4th attempt) = 60 points, not 70
