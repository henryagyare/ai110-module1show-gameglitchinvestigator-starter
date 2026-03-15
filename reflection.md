# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    * Looked like a normal Strealmlit web app clean interface with buttons and typing area for user's guesses
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").
    * Hitting the Enter key does not submit my guess/answer
    * The hints to help converge at the secret answer were not helpful.
      	When I run the app and checked the debug info... I noticed the secret was 38, however when I put 55, I was asked to go higher. And when I put 115.. I was asked to go even higher despite the system limit being 100.
    * There is no message to prompt you that the guess must be within 1 to 100.
        When I entered 115, system still asked me to go higher
    * After winning, I clicked on new game. However, there's a message below that says "You already won. Start a new game to play again." 
        I clicked on the new game button multiple times, but the message doesn't leave even though the secret number and attempt reset everytime.
    * The scoring system is weird. It shows negative scores for missed attempts and sometimes positive 5 still for missed attempts.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    GitHub Copilot (Raptor mini (Preview) 1x)
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    The AI was great at helping identify the errors in the scoring formula. The AI suggested that we were adding to the score when the attempt number was even, even though the guess was incorrect. I verified this by running the app and confirming (before and after the fix).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    When writing the tests, the AI wrote the tests in a way that was checking an assertion for 45 == -15 + 70 (which is not correct.) According to the formular and the calculation, it should have been 60 instead of 70.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    The tests written collaborative with AI was helpful in boosting confidence in the code quality and system accuracy. I ran further manual end to end tests to ensure correctness of behavior.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    I ran pytest -q on test_game_logic.py, and it showed that the guess comparison and scoring logic work correctly after the fix. One test that failed before was test_score_updates_for_guesses (expected +70 instead of +60), and after fixing the expected value, all tests passed.
- Did AI help you design or understand any tests? How?
    Yes. AI helped me understand the code logic. I collaborated with AI to understand the scoring logic and Go Higher / Go Lower logic. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
In Streamlit, the entire Python script is re-executed from top to bottom every time a user interacts with the app (like clicking a button, moving a slider, or typing in a box). This behavior is called a “rerun.” Because the script restarts each time, normal Python variables reset on every interaction, which means they don’t remember previous values. To keep data between these reruns, Streamlit provides st.session_state, which works like a dictionary that stores information for that user’s session, allowing the app to remember things (like counters, user inputs, or intermediate results) even though the script itself keeps rerunning.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      For me, one strategy I plan to carry along into future projects is writing more unit tests and good use of git
- What is one thing you would do differently next time you work with AI on a coding task?
    Prompt Better and be more collaborative
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I think AI generated code is great, but current models definately need some form of expert or human in the loop!
