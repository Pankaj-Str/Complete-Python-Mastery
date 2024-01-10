import random

def choose_random_word():
    words = ["python", "programming", "challenge", "developer", "cwp", "p4n", "simulation"]
    return random.choice(words)

def shuffle_word(word):
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    return ''.join(shuffled_word)

def play_game():
    original_word = choose_random_word()
    shuffled_word = shuffle_word(original_word)

    print("Welcome to WordGuess Simulator!")
    print("Try to guess the original word by unscrambling the letters.")

    while True:
        print("Shuffled word:", shuffled_word)
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            print("Incorrect. Try again!")

if __name__ == "__main__":
    play_game()
