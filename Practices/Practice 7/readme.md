# Practice 7: Wordle Game

Create a Python program that simulates a simple version of the Wordle game. The program should allow a user to guess a
hidden word and provide feedback on their guesses.

## Requirements:
1. Word Selection
- Create a list of possible words (all 5 letters long).
- Randomly select a word from this list to be the hidden word.

2. User Input
- Prompt the user to guess a 5-letter word.
- Ensure the user's guess is valid (i.e., it is a 5-letter word and exists in the list of possible words).

3. Feedback Mechanism
- For each guess, provide feedback using a dictionary:
  - Correct letters in the correct positions.
  - Correct letters in the wrong positions.
  - Incorrect letters.

4. Attempt Tracking
- Allow the user a maximum of 6 attempts to guess the word.
- Track the number of attempts and display appropriate messages if the word is guessed correctly or if attempts run out.

5. Feedback Example:
- If the hidden word is "APPLE" and the user guesses "ALOHA":
- Correct letters in the correct positions: {'A': [0]}
- Correct letters in the wrong positions: {'L': [3], 'A': [0]}
- Incorrect letters: {'O', 'H'}

6. Colorful feedback (1 additional point):
- Enhance the feedback mechanism by displaying the feedback in color. For example, correct letters in the correct
  positions could be green, correct letters in the wrong positions could be yellow, and incorrect letters could be red.
