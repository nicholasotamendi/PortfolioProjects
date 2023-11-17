import random

def binary_search_game():
    # Set up the range of numbers
    low = 1
    high = 100
    target = random.randint(low, high)

    print("Welcome to the Binary Search Guessing Game!")
    print(f"I'm thinking of a number between {low} and {high}.")

    attempts = 0
    guess = None

    while guess != target:
        guess = (low + high) // 2
        print(f"Is it {guess}?")
        attempts += 1

        user_feedback = input("Enter 'h' if too high, 'l' if too low, 'c' if correct: ").lower()

        if user_feedback == 'h':
            high = guess +1
        elif user_feedback == 'l':
            low = guess - 1
        elif user_feedback == 'c':
            print(f"Yay! I guessed the number {target} in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    binary_search_game()
