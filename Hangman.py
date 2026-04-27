import random

print("Welcome to Hangman!!")

words = [
    "apple", "bridge", "candle", "dragon", "engine",
    "flower", "garden", "hammer", "island", "jungle",
    "kitten", "ladder", "mirror", "needle", "orange",
    "pencil", "queen", "rocket", "sunset", "table",
    "umbrella", "violin", "window", "yellow", "zipper",
    "basket", "castle", "dinner", "elephant", "forest",
    "guitar", "helmet", "igloo", "jacket", "kitchen",
    "lemon", "mountain", "napkin", "ocean", "pillow",
    "rabbit", "school", "tiger", "uncle", "village",
    "wallet", "butter", "cloud", "dream", "earth"
    "airplane", "banana", "beach", "bottle", "button",
    "camera", "carpet", "circle", "cookie", "corner",
    "desert", "doctor", "dollar", "donkey", "drawer",
    "eagle", "engineer", "eraser", "family", "feather",
    "finger", "fire", "fishing", "football", "friend",
    "glasses", "grape", "ground", "handle", "hat",
    "horse", "house", "ice", "jewel", "juice",
    "key", "lake", "lamp", "leaf", "letter",
    "magic", "market", "metal", "monkey", "moon",
    "mouse", "music", "paper", "party", "phone"
]
choice = random.choice(words)
print(f"\nThe word has {len(choice)} letters")
correct_letters = ["_"] * len(choice)
errors = 0
guess = 0
incorrect_letters = []
guessed_letters = []

while True:

    if errors == 1:
        print("\n____")
    if errors == 2:
        print("\n    |")
        print("    |")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 3:
        print("\n    ______")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 4:
        print("\n    ______")
        print("    |    |")
        print("    |")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 5:
        print("\n    ______")
        print("    |    |")
        print("    |    o")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 6:
        print("\n    ______")
        print("    |    |")
        print("    |    o")
        print("    |    |")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 7:
        print("\n    ______")
        print("    |    |")
        print("    |    o")
        print("    |   -|")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 8:
        print("\n    ______")
        print("    |    |")
        print("    |    o")
        print("    |   -|-")
        print("    |")
        print("    |")
        print("  __|__")
    if errors == 9:
        print("\n    ______")
        print("    |    |")
        print("    |    o")
        print("    |   -|-")
        print("    |    /\\")
        print("    |")
        print("  __|__")

    print(f"\nYou have {max(0, 10 - errors)} errors left")
    print(f"\nYour word: {' '.join(correct_letters)}")
    print(f"\nYour incorrect letters: {incorrect_letters}")
    print(f"Your correctly guessed letters: {guessed_letters}")
    letter = input("\nEnter a letter to guess: ").lower()
    string = letter.isalpha()

    if len(letter) == 1 and string == True:

        if letter in guessed_letters or letter in incorrect_letters:
            print("\nYou've guessed that letter already!")
            print("Guess again!")
            continue

        if letter in choice:
            print(f"\nThe word contains {letter} in the {choice.index(letter) + 1}º position")
            guessed_letters.append(letter)
            for i, char in enumerate(choice):
                if char == letter:
                    correct_letters[i] = char
            yes = input("Do you want to guess a word (y/n): ").lower()
            if yes == "y":
                guess = input("Enter a word to guess: ")
                if choice == guess:
                    print("You guessed the word!")
                    exit()
                else:
                    print("You guessed wrong.")
                    errors += 1
                    if errors == 10 or errors > 10:
                        print("You lost!!")
                        print(f"The word was {choice}")
                        exit()
            else:
                continue

        elif letter not in choice:
            incorrect_letters.append(letter)
            errors += 1

            if errors == 10 or errors > 10:
                print("You lost!!")
                print(f"The word was {choice}")
                exit()
            print("\nThat letter is not in the word")
            yes = input("Do you want to guess a word (y/n): ").lower()
            if yes == "y":
                guess = input("Enter a word to guess: ")
                if choice == guess:
                    print("You guessed the word!")
                    exit()
                else:
                    print("You guessed wrong. Try again.")
                    errors += 1
                    if errors == 10 or errors > 10:
                        print("You lost!!")
                        print(f"The word was {choice}")
                        exit()

            else:
                continue
    else:
        print("Invalid input")
        continue
