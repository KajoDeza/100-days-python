print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''' )
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
choice_1 = input('You \'re at a crossroad, where do you want to go? Type "right" or "left" ').lower()

if choice_1 == "left":
    choice_2 = input('You have arrived to a lake. '
                     'The island is in the middle of the lake. '
                     'Type "wait" to wait for a boat or type "swim" to swim to the shore" ').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrived at the island unharmed. "
                         "There is a house with a red, yellow and blue door. "
                         "Which one do you choose? ").lower()
        if choice_3 == "red":
            print("It is a room full of fire. Game  over!")
        elif choice_3 == "yellow":
            print("Congrats! You found the treasure!")
        elif choice_3 == "blue":
            print("You have entered a room full of beats. Game over!")
        else:
            print("You chose a door that does not exist. Game over!")
    else:
        print("You got attacked by a crocodile. Game over!")
else:
    print("You fell into a hole. Game over!")








