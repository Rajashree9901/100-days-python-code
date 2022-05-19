import random
from art import logo
from art import vs
from game_data import data
from replit import clear

print(logo)

ch=True

a=random.choice(data)

def compare(i,j):
  if i>j:
    return True
  else:
    return False

s=0

while ch:
  print(f"\nCompare A: {a['name']}, {a['description']}, {a['country']}")
  i=a['follower_count']
  print(vs)
  b=random.choice(data)
  
  while a==b:
    b=random.choice(data)
  print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")
  c=input("who has more followers?: ").lower()
  if c=='a':
    i=a['follower_count']
    j=b['follower_count']
    if compare(i,j):
      s+=1
      print(f"Your current score is {s}")
    else:
      print(f"Game over! Your score is {s}")
      break
  else:
    j=a['follower_count']
    i=b['follower_count']
    if compare(i,j):
      a=b
      s+=1
      print(f"Your current score is {s}")
    else:
      print(f"Sorry that's wrong, your final score is {s}")
      break
  clear()
  print(logo)

    
  
