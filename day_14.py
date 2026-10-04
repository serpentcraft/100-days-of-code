import art
import random
from game_data import data

print(art.logo)

def comparing(option_a, option_b):
    ''' Compare options and returns A or B - who has more followers. '''
    if option_a['follower_count'] > option_b['follower_count']:
        return 'A'
    return 'B'

def get_random_option(exclude=None):
    ''' Returns a random option, not equal to exclude. '''
    options = [x for x in data if x != exclude]
    return random.choice(options)

def game(option_a, option_b):
    ''' Show options, ask user to guess higher or lower, return True or False. '''
    print(f"Compare A: {option_a['name']}, {option_a['description']}, {option_a['country']}")
    print(art.vs)
    print(f"Against B: {option_b['name']}, {option_b['description']}, {option_b['country']}")

    while True:
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_guess in ('A', 'B'):
            break
        print("Please respond with 'A' or 'B'")

    higher = comparing(option_a, option_b)
    return user_guess == higher

score = 0
playing = True
option_a = get_random_option()
option_b = get_random_option(exclude=option_a)

while playing:
    if game(option_a, option_b):
        score += 1
        print(f"Correct! Score: {score}")
        option_a = option_b
        option_b = get_random_option(exclude=option_a)
    else:
        print(f"Wrong! Final score: {score}")
        playing = False
