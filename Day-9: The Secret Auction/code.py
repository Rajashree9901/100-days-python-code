from replit import clear    #FOR CLEAR() FUNCTION

from art import logo
print(logo)

c=True
d={}

while c:
  name=input("What's your name?\n")
  bid=input("Your bid is?\n")
  d[name]=bid
  # print(d)
  p=input("Are there anymore bidders? 'yes' or 'no'\n").lower()
  if p=='no':
    c=False
  clear()

min=0
n=""

for key in d:
  if int(d[key])>min:
    min=int(d[key])
    n=key

print(f"{n} won the bid with {min}")
