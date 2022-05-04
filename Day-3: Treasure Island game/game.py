# This a simple python code build using only if and else

# code

# The ASCII art is picked from  https://ascii.co.uk/art

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice=input("Where are you headed? left or right?\n")
if choice.lower()=="left":
  help=input("You met a creature! Would you like to take help? yes or no?")
  if help.lower()=="yes":
    print("Game Over!\nYou got eaten by the creature :'(\nYou need to be self sufficient! Don't go around asking help. ")
  else:
    door=int(input("You found three doors!\nWhich one do you want to enter? 1 or 2 or 3"))
    if door==1:
      print("Game Over!\nI guess you are not stronger than a tiger!")
    elif door==2:
      print("Game Over!\nYou met the runaway Princess, now you can have a happily ever after!\nYou couldn't get the treasure though, lol!")
    else:
      print("You Won!\nYou found the Treasure! Enjoyyyy!!!")
else:
  print("Game Over!\nEvery right in life is not always right, Sorry!")

