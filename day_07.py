import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

print("\nWelcome to the Hangman Game!")
print("\nThe rules are simple. You need to guess a word (category: animal).\nYou have 6 lives...out of it? You are hanged.\n")

word_list = ['aardvark', 'platypus', 'echidna', 'meerkat', 'orangutan', 'hedgehog', 'narwhal', 'chimpanzee', 'skunk', 'lynx', 'mole', 'sloth', 'hyena', 'koala']

while True:
    lives = 6
    chosen_word = random.choice(word_list)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    game_over = False
    correct_letters = []
    guessed_letters = []

    while not game_over:

        print(f"**************************** {lives}/6 LIVES LEFT ****************************")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter one letter!")
            continue

        if not guess.isalpha():
            print("It is not a letter!")
            continue

        if guess in guessed_letters:
            print("You have already used this letter. Try another one.")
            continue

        guessed_letters.append(guess)

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"Your guess: {guess} - That's not in the word.  You lose a life.")

            if lives == 0:
                game_over = True
                print(f"***********************YOU LOSE**********************")
                print(f"Correct word was - {chosen_word}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(stages[lives])

    play_again = input("\nWanna play one more time? (y/n): ").lower()

    if play_again != "y":
        print("Have a nice day!")
        break
