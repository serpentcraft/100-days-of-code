import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_stops_at = 17

start_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_choice == 'y':
    print(art.logo)
else:
    exit()

def user_playing():
    user_cards = random.choices(cards, k=2)
    score = sum(user_cards)
    print(f" Your cards: {user_cards}. Total: {score}")

    if score >= 21:
        return user_cards, score

    while True:
        hit_choice = input("Do you want another card? (y/n): ").lower()
        if hit_choice == "y":
            user_cards.append(random.choice(cards))
            score = sum(user_cards)
            print(f" Your cards: {user_cards}. Total: {score}")
            if score > 21:
                print("Bust!")
                break
        else:
            break

    return user_cards, score

def computer_playing():
    computer_cards = random.choices(cards, k=2)
    computer_score = sum(computer_cards)
    print(f" Computer first card is: {computer_cards[0]}")

    while computer_score < dealer_stops_at:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

    return computer_cards, computer_score

def determine_winner(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Both busted. It's a draw!"
    if user_score > 21:
        return "You lose!"
    if computer_score > 21:
        return "You win!"
    if user_score > computer_score:
        return "You win!"
    if computer_score > user_score:
        return "You lose!"
    else:
        return "Draw!"

def game_blackjack():
    user_cards, user_score = user_playing()
    computer_cards, computer_score = computer_playing()
    print(f"Computer final hand: {computer_cards}, score: {computer_score}")
    print(determine_winner(user_score, computer_score))

playing = True
while playing:
    game_blackjack()

    while True:
        continue_game = input("Play one more time? (y/n): ").lower()
        if continue_game in ('y', 'n'):
            break
        print("Please enter 'y' or 'n'.")

    if continue_game == 'y':
        print("\n" * 20)
        print(art.logo)
    else:
        playing = False
