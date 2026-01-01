import random

# Predefined word list (fixed scope as required)
WORDS = ["python", "hangman", "coding", "intern", "project"]

MAX_WRONG_GUESSES = 6


def hangman():
    print("\n==============================")
    print("   WELCOME TO HANGMAN GAME")
    print("==============================")

    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    # Create initial hidden word
    display_word = ["_"] * len(secret_word)

    while wrong_guesses < MAX_WRONG_GUESSES and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", " ".join(guessed_letters))
        print(f"Remaining attempts: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Correct guess!")
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    display_word[index] = guess
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1

    # Game result
    print("\n==============================")
    if "_" not in display_word:
        print("🎉 CONGRATULATIONS! YOU WON 🎉")
        print("The word was:", secret_word)
    else:
        print("💀 GAME OVER")
        print("The word was:", secret_word)
    print("==============================\n")


# Run the game
hangman()
