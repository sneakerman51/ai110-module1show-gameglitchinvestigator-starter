# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
60        Too high            Too low           None
new game  refresh values    only secret refreshes none

Attempts left displays 1 higher than actual attempts remaining
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
if guess > secret:
    return "Too High", "📉 Go LOWER!"
else:
    return "Too Low", "📈 Go HIGHER!"
Fixed the inverted logic and I verified it logically and tested it manually and with pytest
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
"3. Secret ignores difficulty
New game hardcodes random.randint(1, 100) — ignores current difficulty. Hard mode range should be 1-50, Easy 1-20, but new game always picks 1-100."
This was slightly misleading because it is true that before it ignored difficulty but when switching in between difficulty with an active game present could also cause secret to be out of bounds.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
testing through pytest and manually on the streamlit
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the pytest without refactoring which helped me realize i forgot to refactor logic_utils.py
- Did AI help you design or understand any tests? How?
AI created my tests and logically explained what each test did and why it would fail if it did
---

## 4. What did you learn about Streamlit and state?

Streamlit reruns your entire script every time someone clicks a button. Any variable you declared at the top gets reset to its starting value, which is why the secret number kept changing. It wasn't a logic bug. The app was just starting over.

`st.session_state` is a dictionary that survives those reruns. 
```

`session_state` is the one place that doesn't get wiped.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
