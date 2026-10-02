import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def play_game():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level in ('easy', 'hard'):
            break
        print("Please enter 'easy' or 'hard'.")

    attempts = 0
    if level == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to make a guess.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to make a guess.")

    secret_number = random.randint(1, 100)

    while attempts > 0:

        while True:
            try:
                guess = int(input("Make a guess: "))
                break  # ← если int() сработал — выходим
            except ValueError:
                print("Please enter a valid number.")

        if guess == secret_number:
            print("You guessed the number. Congratulations!")
            print(art.result_win)
            return "win"
        elif guess > secret_number:
            attempts -= 1
            print("Too high!")
            print(f"You have {attempts} attempts left")
        else:
            attempts -= 1
            print("Too low!")
            print(f"You have {attempts} attempts left")
        if attempts == 0:
            print(f"You don't have any attempts left. Secret number was {secret_number}")
            print(art.result_lose)
            return "lose"

playing = True
while playing:
    result = play_game()
    print(f"You {result}!")

    while True:
        choice = input("Play again? (y/n): ").lower()
        if choice in ('y', 'n'):
            break
        print("Please enter 'y' or 'n'.")

    if choice != 'y':
        playing = False
