from art import logo
import random

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player=[]
comp=[]

print(logo)
player.append(random.choice(cards))
player.append(random.choice(cards))  
comp.append(random.choice(cards))
comp.append(random.choice(cards))

ch=True
p=0
q=0

sump=sum(player)
sumc=sum(comp)
print(f"Your cards: {player}, current score {sump}")
print(f"Computer's first card: {comp[0]}")

while ch:
  sump=sum(player)
  sumc=sum(comp)
  
  if sump==21:
    print("You got BlackJack!")
    print("You Win!")
    q=1
    break
  if sumc==21:
    print(f"Computer's card are: {comp}, Computer has BlackJack!")
    print("Computer won!")
    p=1
    break

  if sump>21:
    if 11 in player:
      i=player.index(11)
      player[i]=1
      print("Ace's value is taken to be 1!")
      print(f"Your cards now: {player}, score: {sum(player)}")
    else:
      print("You Lose!")
      p=1
      break
  else:
    if input("Do you want to pick another card? y or n: ")=="n":
      ch=False
    else:
      player.append(random.choice(cards))
      print(f"your current cards: {player},current score: {sum(player)}")
    
while sum(comp)<17:
  x=random.choice(cards)
  if x==11 and sum(comp)>21:
    x=1
  comp.append(x)

if p!=1 and q!=1:
  if sum(comp)>21:
    print(f"Computer's cards: {comp}, current computer's score {sum(comp)}")
    print("You Win!")
  elif sum(player)>sum(comp):
    print(f"Computer's cards: {comp}")
    print("You Win!")
  elif sum(player)==sum(comp):
    print(f"Computer's cards:{comp}, score:{sum(comp)}")
    print("Draw!")
  else:
    print(f"Computer's cards: {comp}")
    print("You Lose!")
    
