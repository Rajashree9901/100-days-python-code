# Tip Calculator

# Welcome Message
print("Welcome to the tip Calculator!\n\n")

# taking inputs
bill=int(input("What was your total bill?\nRs "))
tip=int(input("What percentage of tip do you want to give?(10,12,15)\n"))
n=int(input("How many people are splitting the bill?\n"))

# Calculating individual bills
s= (bill*tip)/(100)
s+=bill
s/=n
s=round(s,2)

print(f"Each person should pay Rs {s}")
