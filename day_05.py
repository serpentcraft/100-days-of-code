# 2026_09_19 day 5 of 100 days of Code
# It was a brain-teaser, but it gave me an opportunity to look
# for things on my own, to use python documentation etc.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?(max 52)\n"))
nr_symbols = int(input(f"How many symbols would you like?(max 9)\n"))
nr_numbers = int(input(f"How many numbers would you like?(max 10)\n"))

if nr_letters > len(letters) or nr_numbers > len(numbers) or nr_symbols > len(symbols):
    print("Your choice is too big, please enter another amount!")
else:
    password = ""
    for _ in range(nr_letters):
        password += random.choice(letters)
    for _ in range(nr_symbols):
        password += random.choice(symbols)
    for _ in range(nr_numbers):
        password += random.choice(numbers)
    print(f"Your password is: {password}")
    password_list = list(password)
    random.shuffle(password_list)
    shuffled = "".join(password_list)
    print(f"Your shuffled password is: {shuffled}")
