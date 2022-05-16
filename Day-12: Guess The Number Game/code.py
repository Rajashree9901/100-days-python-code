import random
from art import logo
print(logo)

num=random.randint(1,100)
# print(num)

def check(g):
  if g<num:
    return 0
  elif g>num:
    return 2
  else:
    return 1
  
print("Guess a number between 1 and 100.")
if input("choose the difficulty level: Hard or Easy\n").lower()=="hard":
  chances=5
else:
  chances=10

f=0
while chances>0 :
  print(f"You have {chances} chances remaining")
  guess=int(input())
  chances=chances-1
  c=check(guess)
  if c==0:
    print("Too Low!")
  elif c==2:
    print("Too High!")
  else:
    print(f"You guessed it right! The number is {guess}")
    f=1
    break
  if f!=1 and chances!=0:
    print("Guess again!")

if f==0:
  print("You couldn't get the right number, You Lose!")
