from logic_utils import check_guess

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug: backwards hint messages ---

def test_too_high_message_says_go_lower():
    # Bug: was returning "Go HIGHER!" when guess > secret
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_too_low_message_says_go_higher():
    # Bug: was returning "Go LOWER!" when guess < secret
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"


# --- Bug: string-secret comparison on even attempts ---
# On even attempt numbers, app.py converts secret to str before check_guess.
# check_guess must handle str secret correctly (not flip logic via string comparison).

def test_check_guess_with_string_secret_win():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_with_string_secret_too_high():
    # guess=60, secret="50" — str comparison "60" > "50" is True, so outcome must still be Too High
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_with_string_secret_too_low():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
