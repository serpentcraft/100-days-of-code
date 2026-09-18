import random
# ASCII art
rock = '''             
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Game
art = [rock, paper, scissors]
options = ['Rock', 'Paper', 'Scissors']

print("Welcome to Rock Paper Scissors!")
try:
    human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
except ValueError:
    print("Please enter a number!")
    exit()
if human not in [0, 1, 2]:
    print("You did silly thing. Please try again.")
else:
    computer = random.randint(0,2)

    print(f"You chose: {options[human]}")
    print(art[human])
    print(f"Computer chose: {options[computer]}")
    print(art[computer])

    if human == computer:
        print("That's a draw!\nTry again")
    elif (human - computer) % 3 == 1:
        print("You won!")
    else:
        print("You lost!")
