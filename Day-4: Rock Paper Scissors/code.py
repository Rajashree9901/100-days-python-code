# importing random module for the computer to choose it's play
import random

# ASCII art picked from https://ascii.co.uk/art
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

# user input
c=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if c==0:
  print(rock)
elif c==1:
  print(paper)
else:
  print(scissors)

x=random.randint(1,2)
print("MY choice:")

if c<0 or c>2:
  print("Invalid choice!")
else:
  if x==0:
    print(rock)
    if c==x:
      print("Draw!")
    elif c==1:
      print("You Win!")
    else:
      print("You Lose!")
  elif x==1:
    print(paper)
    if c==x:
      print("Draw!")
    elif c==2:
      print("You Win!")
    else:
      print("You Lose!")
  else:
    print(scissors)
    if c==x:
      print("Draw!")
    elif c==0:
      print("You Win!")
    else:
      print("You Lose!")
