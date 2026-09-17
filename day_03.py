# Also it contained ascii art treasure island, but I didn't put it here 

import random

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

winning_door = random.choice(["red", "yellow", "blue"])

choice_1 = input("You've arrived at Treasure Island. Do you check the dense jungle first, or the wrecked boat out at sea?\nType: jungle or boat ").lower()
if choice_1 == "jungle":
    print("You suffer a fatal python attack. Game over.")
elif choice_1 == "boat":
    print("You continue your journey.")
    choice_2 = input("You meet a grumpy goblin. He suggests swimming out to check the boat. He says he saw something sparkly out there.\n Will you swim with him, or wait for him on the shore?\nType: swim or wait ").lower()
    if choice_2 == "swim":
        print("The sparkly thing turns out to be a jellyfish. Not your smartest move — you're dead. Game over.")
    elif choice_2 == "wait":
        print("You wait for the goblin, but he's nowhere to be seen. Poor bastard.")
        choice_3 = input("Instead, you walk away from the shore and find a cave. Inside, there are three doors. Above them, an inscription reads: 'Only one may be opened. Which one do you choose?\nType: red, yellow or blue ").lower()
        if choice_3 == winning_door:
            print("You see a huge chest filled with coins and gems. You're rich now! Congratulations!")
        elif choice_3 in ["red", "yellow", "blue"]:
            print("This is not your lucky day. You see an evil creature who's not happy to be woken up. Game over.")
        else:
            print("You hesitated and the cave collapsed. Game over.")

else:
    print("You wandered off and got lost. Game over.")
