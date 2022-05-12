from art import logo

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def square(a,b):
  return a**b

operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
  "**":square
}

def calc():
#   to clear the screen of replit ide
  from replit import clear
  clear()
  print (logo)
  a=float(input("The first number is:"))
  for key in operations:
    print(key)
  
  c=True
  while c:
    x=input("Pick an operation\n")
    b=float(input("The second number is:"))
    for key in operations:
      if key==x:
        ans=operations[key](a,b)
        print(f"{a} {key} {b} = {ans}")
    
    if input("Press y to continue and n to restart the calculations:")=="y":
      a=ans
    else:
      c=False
      calc()

calc()
