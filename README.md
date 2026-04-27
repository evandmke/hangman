# hangman
Hangman Game

A text-based Hangman game written in Python where the player tries to guess a hidden word letter by letter before running out of attempts.

How to Play

Run the program — a random word will be chosen and you'll be told how many letters it has
Enter one letter at a time to guess
If the letter is in the word, its position will be revealed
After each guess, you can choose to guess the full word
You have 10 errors before the hangman is complete and you lose

Rules

Only single letters are accepted as input
Numbers and special characters are rejected
Already guessed letters (correct or incorrect) are tracked and cannot be re-entered
Guessing the full word wrong counts as an error
Guessing the full word correctly wins the game instantly

Losing Condition
The game ends when you reach 10 errors. The hangman drawing builds progressively with each mistake.
