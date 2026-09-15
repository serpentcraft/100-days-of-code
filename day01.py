#I wanted to make it a bit more interactive and fun, so I used some things that I learned couple of days ago, mostly I wanted to practice using it.
  
from time import sleep
string = "Welcome to the Band Name Generator!"
for letter in string:
 print(letter, end="", flush=True)
 sleep(0.2)
print()
string = "\nYou will be asked two simple questions."
for letter in string:
 print(letter, end="", flush=True)
 sleep(0.2)
print()
string = "\nAnd this will be your band name."
for letter in string:
 print(letter, end="", flush=True)
 sleep(0.2)
print()
answer = input("Continue? [y/n]: ")
if answer.lower() == "y":
 city = input("What is the name of your city you grew up in? \n")
 pet = input("What is the name of your pet? \n")
 print(f"Congratulations! Your band name is {city}, {pet}.\nEnjoy!")
else:
 print("Then I have to say good luck figuring it out on your own!")
