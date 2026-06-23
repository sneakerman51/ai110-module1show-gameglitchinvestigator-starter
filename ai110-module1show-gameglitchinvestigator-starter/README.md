# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A number-guessing game where the player guesses a secret integer within a chosen difficulty range. The app gives higher/lower hints and tracks a score across attempts.

**Bugs found:**
1. **State bug** — the secret number was regenerated on every Streamlit re-run (every button click), making it impossible to win. Fixed by storing it in `st.session_state` on first run only.
2. **Logic bug** — hint messages were backwards: "Go HIGHER" when the guess was too high, "Go LOWER" when too low. Fixed in `check_guess()` in `logic_utils.py`.

**Fixes applied:** Moved game logic into `logic_utils.py`; corrected the direction strings in `check_guess`; initialized `st.session_state.secret` with a guard so it persists across re-runs.

## 📸 Demo Walkthrough

1. User opens the app — the secret number is generated once and stored in `st.session_state`, so it stays fixed for the entire round regardless of how many times the user clicks Submit.
2. User selects difficulty "Normal" (range 1–100) and enters a guess of `40` → game returns **"📈 Go HIGHER!"** (Too Low).
3. User enters `70` → game returns **"📉 Go LOWER!"** (Too High). Score updates after each guess.
4. User enters `55` → game returns **"📈 Go HIGHER!"** (Too Low). Score updates again.
5. User enters `63` → game returns **"🎉 Correct!"** Final score is displayed.
6. User clicks **Play Again** — session state resets, a new secret number is generated, and the game restarts.

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0 -- python.exe
cachedir: .pytest_cache
rootdir: ...\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED     [ 50%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED     [ 62%]
tests/test_game_logic.py::test_check_guess_with_string_secret_win PASSED [ 75%]
tests/test_game_logic.py::test_check_guess_with_string_secret_too_high PASSED [ 87%]
tests/test_game_logic.py::test_check_guess_with_string_secret_too_low PASSED [100%]

============================== 8 passed in 0.12s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
